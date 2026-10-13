#!/usr/bin/env python3
"""Deterministic citation verifier.

usage: python3 -I verify_candidates.py CANDIDATES.json OUT.json --chapter A01 --title 质膜 --part A [--meta META.json] [--append]

CANDIDATES.json : list of {title, first_author, year, doi, journal, kind, subtopic, key_finding_zh, why_it_matters_zh, importance}
OUT.json        : {chapter_id, chapter_title, part, n_verified, papers:[...], key_concepts_zh, open_questions_zh, cross_disciplinary_hooks_zh}
META.json       : optional {key_concepts_zh:[], open_questions_zh:[], cross_disciplinary_hooks_zh:[]} merged into OUT
--append        : merge into an existing OUT.json (skip DOIs already present), tag new entries note="round2"

For every candidate: CrossRef by DOI -> title similarity >= 0.85 => verified (authoritative metadata overwrites).
Otherwise CrossRef bibliographic search (title + first author + year); best hit >= 0.85 => corrected; else dropped.
Abstract/PMID from Europe PMC, fallback OpenAlex; cited_by_count from OpenAlex.
Prints a compact report and writes OUT.report.json next to OUT.json.
"""
import argparse, difflib, json, re, sys, time, urllib.parse, urllib.request, urllib.error

UA = 'memlit-verify/1.0'
SLEEP = 0.2


def get_json(url, tries=3, timeout=25):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode('utf-8', 'replace'))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                return {'__error__': 'rate_limited', '__429__': True}
            last = e
        except Exception as e:  # noqa
            last = e
        time.sleep(0.8 * (i + 1))
    return {'__error__': str(last)}


def norm_doi(d):
    s = (d or '').strip().lower()
    s = re.sub(r'^https?://(dx\.)?doi\.org/', '', s)
    s = re.sub(r'^doi:\s*', '', s)
    s = s.rstrip(' .;,)')
    return s


def norm_title(t):
    return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()


def sim(a, b):
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


BAD_TYPES = {'component', 'dataset', 'peer-review', 'grant', 'standard', 'database', 'report-component'}


def bad_record(m):
    if not m:
        return 'empty'
    if m.get('cr_type') in BAD_TYPES:
        return 'crossref type ' + str(m.get('cr_type'))
    if re.match(r'^(fig|figure|table|supplementary|supplemental|appendix|correction|erratum|corrigendum|retraction|retracted|author correction|publisher correction|expression of concern)\b', norm_title(m.get('title'))):
        return 'figure/table record'
    if re.match(r'^\d+a(\s*-\s*\d+a)?$', str(m.get('page') or '').strip()):
        return 'meeting abstract (page %s)' % m.get('page')
    return ''


def title_match(cand, auth):
    a, b = norm_title(cand), norm_title(auth)
    if not a or not b:
        return 0.0
    s = difflib.SequenceMatcher(None, a, b).ratio()
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    if len(short) >= 25 and long_.startswith(short):
        s = max(s, 0.9)
    return s


def year_ok(cy, my, tol):
    try:
        return not cy or not my or abs(int(cy) - int(my)) <= tol
    except Exception:
        return True


def cr_author(a):
    fam = a.get('family') or a.get('name') or ''
    giv = a.get('given') or ''
    ini = ''.join(w[0] for w in re.split(r'[\s\-]+', giv) if w)
    return (fam + (' ' + ini if ini else '')).strip()


def parse_crossref(m):
    title = (m.get('title') or [''])[0]
    authors = m.get('author') or []
    year = None
    for k in ('published-print', 'published-online', 'issued', 'created'):
        dp = (m.get(k) or {}).get('date-parts') or []
        if dp and dp[0] and dp[0][0]:
            year = dp[0][0]
            break
    return {
        'title': title,
        'first_author': cr_author(authors[0]) if authors else '',
        'last_author': cr_author(authors[-1]) if len(authors) > 1 else '',
        'year': year,
        'journal': (m.get('container-title') or [''])[0] or (m.get('publisher') or ''),
        'doi': norm_doi(m.get('DOI')),
        'cr_type': m.get('type'),
        'page': m.get('page') or '',
        'cr_abstract': m.get('abstract') or '',
    }


def crossref_by_doi(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='')
    d = get_json(url)
    if not d or '__error__' in d:
        return None
    return parse_crossref(d.get('message', {}))


def crossref_search(title, author, year):
    q = f"{title} {author or ''} {year or ''}".strip()
    url = 'https://api.crossref.org/works?rows=5&query.bibliographic=' + urllib.parse.quote(q)
    d = get_json(url)
    if not d or '__error__' in d:
        return []
    return [parse_crossref(it) for it in (d.get('message', {}).get('items') or [])]


def europepmc(doi):
    q = urllib.parse.quote(f'DOI:"{doi}"')
    url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json&resultType=core&pageSize=1'
    d = get_json(url)
    if not d or '__error__' in d:
        return {}
    res = (d.get('resultList') or {}).get('result') or []
    if not res:
        return {}
    r = res[0]
    return {'abstract': r.get('abstractText') or '', 'pmid': r.get('pmid') or '', 'cited_by_count': r.get('citedByCount')}


DISABLED = {'openalex': False, 's2': 0}


def semantic_scholar(doi):
    if DISABLED['s2'] >= 3:
        return {}
    url = 'https://api.semanticscholar.org/graph/v1/paper/DOI:' + urllib.parse.quote(doi, safe='/') + '?fields=abstract,citationCount'
    d = get_json(url, tries=1)
    if not d:
        return {}
    if d.get('__429__'):
        DISABLED['s2'] += 1
        time.sleep(2)
        return {}
    if '__error__' in d:
        return {}
    return {'abstract': d.get('abstract') or '', 'cited_by_count': d.get('citationCount')}


def openalex(doi):
    if DISABLED['openalex']:
        return {}
    url = 'https://api.openalex.org/works/https://doi.org/' + doi
    d = get_json(url, tries=1)
    if d and d.get('__429__'):
        DISABLED['openalex'] = True
        print('[info] OpenAlex rate-limited; disabled for this run')
        return {}
    if not d or '__error__' in d:
        return {}
    inv = d.get('abstract_inverted_index')
    abstract = ''
    if inv:
        pos = {}
        for w, idxs in inv.items():
            for i in idxs:
                pos[i] = w
        abstract = ' '.join(pos[i] for i in sorted(pos))
    return {'abstract': abstract, 'cited_by_count': d.get('cited_by_count')}


def strip_html(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('candidates')
    ap.add_argument('out')
    ap.add_argument('--chapter', required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--part', required=True)
    ap.add_argument('--meta')
    ap.add_argument('--append', action='store_true')
    ap.add_argument('--note', default='')
    a = ap.parse_args()

    with open(a.candidates, encoding='utf-8') as f:
        cands = json.load(f)
    if isinstance(cands, dict):
        cands = cands.get('papers', [])

    existing = {'papers': []}
    if a.append:
        try:
            with open(a.out, encoding='utf-8') as f:
                existing = json.load(f)
        except Exception:
            existing = {'papers': []}
    have = {norm_doi(p.get('doi')): p for p in existing.get('papers', [])}
    have_titles = {norm_title(p.get('title')): p for p in existing.get('papers', [])}

    out_papers, dropped, corrected, verified = [], [], 0, 0
    seen = {}
    n_abs = 0
    for i, c in enumerate(cands):
        doi = norm_doi(c.get('doi'))
        title = c.get('title') or ''
        meta = None
        status = None
        note = []
        if doi:
            m = crossref_by_doi(doi)
            time.sleep(SLEEP)
            br = bad_record(m) if m else ''
            ts = title_match(title, m['title']) if m else 0
            fa = ((c.get('first_author') or '').split() or [''])[0].lower()
            if m and br:
                note.append('doi_rejected: ' + br)
            elif m and ts >= 0.85 and year_ok(c.get('year'), m.get('year'), 3):
                meta, status = m, 'verified'
            elif m and ts >= 0.70 and c.get('year') and m.get('year') and year_ok(c.get('year'), m.get('year'), 1) and fa and fa in (m.get('first_author') or '').lower():
                meta, status = m, 'verified'
                note.append(f"title_sim={ts:.2f} accepted by author+year")
            elif m and len(norm_title(m['title'])) >= 6 and norm_title(title).startswith(norm_title(m['title'])) and year_ok(c.get('year'), m.get('year'), 0) and fa and fa in (m.get('first_author') or '').lower():
                meta, status = dict(m, title=title), 'verified'
                note.append(f"crossref title truncated ('{m['title']}'); accepted by prefix+author+year")
            else:
                note.append('doi_mismatch' if m else 'doi_not_found')
        if meta is None:
            hits = crossref_search(title, c.get('first_author'), c.get('year'))
            time.sleep(SLEEP)
            best, best_s = None, 0
            for h in hits:
                if bad_record(h) or not year_ok(c.get('year'), h.get('year'), 2):
                    continue
                s = title_match(title, h['title'])
                if s > best_s:
                    best, best_s = h, s
            if best and best_s >= 0.85:
                meta, status = best, 'corrected'
                note.append(f'doi corrected {doi or "(none)"} -> {best["doi"]} (sim {best_s:.2f})')
            else:
                dropped.append({'title': title, 'doi': doi, 'reason': 'not found in CrossRef (best sim %.2f)' % best_s})
                print(f'[DROP] {title[:80]} | {doi} | best sim {best_s:.2f}')
                continue
        if c.get('year') and meta.get('year') and abs(int(c['year']) - int(meta['year'])) > 1:
            note.append(f"year {c.get('year')} -> {meta.get('year')}")
        d2 = meta['doi']
        if d2 in have or norm_title(meta['title']) in have_titles:
            dropped.append({'title': meta['title'], 'doi': d2, 'reason': 'already in chapter JSON'})
            print(f'[SKIP already present] {meta["title"][:80]}')
            continue
        if d2 in seen:
            prev = seen[d2]
            if (c.get('importance') or 0) > (prev.get('importance') or 0):
                prev['importance'] = c.get('importance')
            print(f'[DUP merged] {meta["title"][:80]}')
            continue
        ep = europepmc(d2)
        time.sleep(SLEEP)
        abstract = strip_html(ep.get('abstract') or meta.get('cr_abstract') or '')
        cites = ep.get('cited_by_count')
        oa = {}
        if not abstract or cites is None:
            oa = openalex(d2)
            time.sleep(SLEEP)
            abstract = abstract or strip_html(oa.get('abstract') or '')
            cites = cites if cites is not None else oa.get('cited_by_count')
        if not abstract:
            s2 = semantic_scholar(d2)
            time.sleep(1.0)
            abstract = strip_html(s2.get('abstract') or '')
            cites = cites if cites is not None else s2.get('cited_by_count')
        oa = {'cited_by_count': cites}
        if abstract:
            n_abs += 1
        else:
            note.append('abstract_unavailable')
        p = {
            'title': meta['title'], 'first_author': meta['first_author'] or c.get('first_author', ''),
            'last_author': meta['last_author'] or c.get('last_author', ''), 'year': meta['year'] or c.get('year'),
            'journal': meta['journal'] or c.get('journal', ''), 'doi': d2, 'pmid': ep.get('pmid') or '',
            'kind': c.get('kind', 'primary'), 'subtopic': c.get('subtopic', ''), 'key_finding_zh': c.get('key_finding_zh', ''),
            'why_it_matters_zh': c.get('why_it_matters_zh', ''), 'importance': c.get('importance', 3),
            'abstract': abstract[:1500], 'cited_by_count': oa.get('cited_by_count'),
            'verification': status, 'note': '; '.join([a.note] + note if a.note else note),
        }
        seen[d2] = p
        out_papers.append(p)
        if status == 'verified':
            verified += 1
        else:
            corrected += 1
        print(f'[{status.upper()[:4]}] {p["first_author"]} {p["year"]} | {p["title"][:70]} | {d2} | abs={"y" if abstract else "n"} | cites={p["cited_by_count"]}')

    meta_extra = {}
    if a.meta:
        with open(a.meta, encoding='utf-8') as f:
            meta_extra = json.load(f)

    def merge_list(key):
        old = existing.get(key, []) if a.append else []
        new = meta_extra.get(key, [])
        outl = []
        for x in old + new:
            if x and x not in outl:
                outl.append(x)
        return outl

    all_papers = (existing.get('papers', []) if a.append else []) + out_papers
    out = {
        'chapter_id': a.chapter, 'chapter_title': a.title, 'part': a.part, 'n_verified': len(all_papers),
        'papers': all_papers,
        'key_concepts_zh': merge_list('key_concepts_zh'),
        'open_questions_zh': merge_list('open_questions_zh'),
        'cross_disciplinary_hooks_zh': merge_list('cross_disciplinary_hooks_zh'),
    }
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    report = {'n_input': len(cands), 'n_verified': verified, 'n_corrected': corrected, 'n_dropped': len(dropped),
              'n_with_abstract': n_abs, 'n_total_in_file': len(all_papers), 'dropped': dropped}
    with open(re.sub(r'\.json$', '', a.out) + '.report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print('REPORT ' + json.dumps({k: v for k, v in report.items() if k != 'dropped'}, ensure_ascii=False))


if __name__ == '__main__':
    main()

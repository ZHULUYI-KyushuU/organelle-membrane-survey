#!/usr/bin/env python3
"""Build 文献总表 (markdown + csv) and corpus stats from the verified chapter JSONs."""
import csv, glob, json, os, sys, collections

DATA_DIR = sys.argv[1]
OUT_DIR = sys.argv[2]

rows = []
by_doi = {}
stats = collections.OrderedDict()
kinds = collections.Counter()
years = collections.Counter()
parts = collections.Counter()
for path in sorted(glob.glob(os.path.join(DATA_DIR, '*.json'))):
    if not __import__('re').match(r'^[A-Z]\d\d\.json$', os.path.basename(path)):
        continue
    try:
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
    except Exception as e:
        print('BAD JSON', path, e, file=sys.stderr)
        continue
    cid = d.get('chapter_id') or os.path.basename(path)[:3]
    title = d.get('chapter_title', '')
    part = d.get('part', cid[:1])
    papers = d.get('papers', [])
    stats[cid] = {'title': title, 'part': part, 'n': len(papers),
                  'verified': sum(1 for p in papers if p.get('verification') == 'verified'),
                  'corrected': sum(1 for p in papers if p.get('verification') == 'corrected'),
                  'round2': sum(1 for p in papers if 'round2' in str(p.get('note', '')))}
    parts[part] += len(papers)
    for p in papers:
        doi = (p.get('doi') or '').lower().strip()
        kinds[p.get('kind', '?')] += 1
        y = p.get('year')
        if isinstance(y, int):
            years[y // 10 * 10] += 1
        row = {
            'chapter': cid, 'part': part, 'first_author': p.get('first_author', ''), 'last_author': p.get('last_author', ''),
            'year': y, 'title': p.get('title', ''), 'journal': p.get('journal', ''), 'doi': doi, 'pmid': p.get('pmid') or '',
            'kind': p.get('kind', ''), 'importance': p.get('importance', ''), 'cited_by_count': p.get('cited_by_count'),
            'subtopic': p.get('subtopic', ''), 'key_finding_zh': p.get('key_finding_zh', ''), 'verification': p.get('verification', ''),
        }
        rows.append(row)
        by_doi.setdefault(doi, []).append(cid)

unique = len([d for d in by_doi if d])
shared = {d: c for d, c in by_doi.items() if d and len(c) > 1}

os.makedirs(OUT_DIR, exist_ok=True)
csv_path = os.path.join(OUT_DIR, '文献总表.csv')
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ['chapter'])
    w.writeheader()
    for r in sorted(rows, key=lambda r: (r['chapter'], -(r['importance'] or 0), -(r['year'] or 0))):
        w.writerow(r)

md_path = os.path.join(OUT_DIR, '文献总表.md')
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('---\ntitle: 文献总表\ntags: [细胞器膜, 酵母, 文献调研, 总表]\n---\n\n')
    f.write(f'# 文献总表\n\n条目 {len(rows)}，去重后唯一 DOI {unique}，跨章共享 DOI {len(shared)}。CSV 版本：文献总表.csv\n\n')
    f.write('## 各章统计\n\n| 章 | 标题 | 文献数 | 核验通过 | 元数据修正 | 二轮补充 |\n|---|---|---|---|---|---|\n')
    for cid, s in stats.items():
        f.write(f"| {cid} | [[{cid}_{s['title']}]] | {s['n']} | {s['verified']} | {s['corrected']} | {s['round2']} |\n")
    f.write('\n## 类型分布\n\n' + ', '.join(f'{k} {v}' for k, v in kinds.most_common()) + '\n\n')
    f.write('## 年代分布\n\n' + ', '.join(f'{k}s {v}' for k, v in sorted(years.items())) + '\n\n')
    f.write('## 全部条目\n\n| 章 | 引用 | 年 | 期刊 | 类型 | 重要性 | 引用数 | 一句话发现 | DOI |\n|---|---|---|---|---|---|---|---|---|\n')
    for r in sorted(rows, key=lambda r: (r['chapter'], -(r['importance'] or 0), -(r['year'] or 0))):
        fa = r['first_author'] or '?'
        cite = f"{fa} et al."
        kf = (r['key_finding_zh'] or '').replace('|', '/').replace('\n', ' ')
        if len(kf) > 120:
            kf = kf[:118] + '…'
        doi = r['doi']
        doi_md = f'[{doi}](https://doi.org/{doi})' if doi else ''
        f.write(f"| {r['chapter']} | {cite} | {r['year']} | {r['journal']} | {r['kind']} | {r['importance']} | {r['cited_by_count'] if r['cited_by_count'] is not None else ''} | {kf} | {doi_md} |\n")

print(json.dumps({'rows': len(rows), 'unique_doi': unique, 'shared_doi': len(shared), 'parts': dict(parts), 'kinds': dict(kinds), 'chapters': len(stats)}, ensure_ascii=False))

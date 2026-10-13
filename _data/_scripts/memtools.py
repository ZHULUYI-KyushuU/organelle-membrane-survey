#!/usr/bin/env python3
"""Helper tools for the organelle-membrane survey (stdlib only).

python3 -I memtools.py digest  DATA_DIR ID            -> DATA_DIR/ID.digest.md  (compact cards for the chapter writer)
python3 -I memtools.py table   DATA_DIR ID MD_PATH    -> (re)writes the "## 本章文献表" section at the end of MD_PATH
python3 -I memtools.py index   DATA_DIR               -> DATA_DIR/_index.md + _index.json (from ID.json + ID.write.json sidecars)
python3 -I memtools.py stats   DATA_DIR               -> prints corpus stats + must-read candidates (compact)
"""
import collections, glob, json, os, re, sys

PART_NAMES = {'A': '生物学核心', 'B': '物理学视角', 'C': '数学视角', 'D': '计算机视角', 'E': '其他视角', 'G': '补充章'}


def load(data_dir, cid):
    with open(os.path.join(data_dir, cid + '.json'), encoding='utf-8') as f:
        return json.load(f)


def chapter_files(data_dir):
    out = []
    for p in sorted(glob.glob(os.path.join(data_dir, '*.json'))):
        b = os.path.basename(p)
        if re.match(r'^[A-Z]\d\d\.json$', b):
            out.append(b[:-5])
    return out


def cite(p):
    fa = (p.get('first_author') or '?').split()[0]
    return f"{fa} et al., {p.get('year')}"


def sort_key(p):
    return (-(p.get('importance') or 0), -(p.get('cited_by_count') or 0), -(p.get('year') or 0))


def digest(data_dir, cid):
    d = load(data_dir, cid)
    ps = d['papers']
    by_sub = collections.OrderedDict()
    for p in sorted(ps, key=sort_key):
        by_sub.setdefault((p.get('subtopic') or '其他').strip(), []).append(p)
    lines = [f"# {cid} {d.get('chapter_title','')} 文献卡片（共 {len(ps)} 篇，已核验）", '',
             '格式：[编号] 引用 | 期刊 | 类型 | 重要性 | 被引 | DOI；下一行为中文发现；重要性 5 的条目附英文摘要节选。', '']
    for k in ('key_concepts_zh', 'open_questions_zh', 'cross_disciplinary_hooks_zh'):
        if d.get(k):
            lines.append(f"**{k}**：" + '；'.join(d[k]))
    lines.append('')
    n = 0
    for sub, items in by_sub.items():
        lines.append(f"## {sub}（{len(items)}）")
        for p in items:
            n += 1
            title = (p.get('title') or '')[:140]
            lines.append(f"[{n}] {cite(p)} | {p.get('journal','')[:40]} | {p.get('kind','')} | {p.get('importance','')} | {p.get('cited_by_count') if p.get('cited_by_count') is not None else ''} | {p.get('doi','')}")
            lines.append(f"    题名：{title}")
            kf = (p.get('key_finding_zh') or '').replace('\n', ' ')
            lines.append(f"    发现：{kf}")
            if (p.get('importance') or 0) >= 5 and p.get('abstract'):
                lines.append(f"    摘要节选：{p['abstract'][:320]}")
        lines.append('')
    out = os.path.join(data_dir, cid + '.digest.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"digest written: {out} ({len(ps)} papers, {sum(len(x) for x in lines)} chars)")


def table(data_dir, cid, md_path):
    d = load(data_dir, cid)
    ps = sorted(d['papers'], key=lambda p: (-(p.get('importance') or 0), -(p.get('year') or 0)))
    rows = ['## 本章文献表', '', f'共 {len(ps)} 篇，全部经 CrossRef 核验 DOI 与题名；按重要性、年份降序。', '',
            '| # | 引用 | 类型 | 重要性 | 一句话发现 | DOI |', '|---|---|---|---|---|---|']
    for i, p in enumerate(ps, 1):
        kf = (p.get('key_finding_zh') or '').replace('|', '／').replace('\n', ' ')
        first = re.split(r'(?<=[。；])', kf)[0] if kf else ''
        if len(first) > 110:
            first = first[:108] + '…'
        doi = p.get('doi', '')
        j = (p.get('journal') or '').replace('|', '／')
        rows.append(f"| {i} | {cite(p)}, *{j}* | {p.get('kind','')} | {p.get('importance','')} | {first} | [{doi}](https://doi.org/{doi}) |")
    with open(md_path, encoding='utf-8') as f:
        text = f.read()
    idx = text.find('\n## 本章文献表')
    if idx != -1:
        text = text[:idx].rstrip() + '\n'
    text = text.rstrip() + '\n\n' + '\n'.join(rows) + '\n'
    text = re.sub(r'(?m)^n_papers:.*$', f'n_papers: {len(ps)}', text, count=1)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"table appended to {md_path}: {len(ps)} rows")


def index(data_dir):
    entries = []
    for cid in chapter_files(data_dir):
        d = load(data_dir, cid)
        w = {}
        wp = os.path.join(data_dir, cid + '.write.json')
        if os.path.exists(wp):
            with open(wp, encoding='utf-8') as f:
                w = json.load(f)
        entries.append({
            'id': cid, 'title': d.get('chapter_title', ''), 'part': d.get('part', cid[0]),
            'file': w.get('file') or f"{cid}_{d.get('chapter_title','')}.md", 'n_papers': len(d['papers']),
            'written': bool(w), 'abstract_zh': w.get('abstract_zh', ''),
            'key_concepts_zh': (w.get('key_concepts_zh') or d.get('key_concepts_zh') or [])[:12],
            'open_questions_zh': (w.get('open_questions_zh') or d.get('open_questions_zh') or [])[:8],
            'cross_hooks_zh': (w.get('cross_hooks_zh') or d.get('cross_disciplinary_hooks_zh') or [])[:8],
        })
    with open(os.path.join(data_dir, '_index.json'), 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    lines = ['# 全书章节索引', '']
    for e in entries:
        lines += [f"## {e['id']} {e['title']}（{PART_NAMES.get(e['part'], e['part'])}，{e['n_papers']} 篇，文件 {e['file']}）",
                  f"摘要：{e['abstract_zh']}",
                  '核心概念：' + '；'.join(e['key_concepts_zh']),
                  '开放问题：' + '；'.join(e['open_questions_zh']),
                  '交叉切入点：' + '；'.join(e['cross_hooks_zh']), '']
    with open(os.path.join(data_dir, '_index.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"index: {len(entries)} chapters, {sum(1 for e in entries if e['written'])} written -> {data_dir}/_index.md")


def stats(data_dir):
    rows, dois = [], collections.defaultdict(set)
    kinds, decades = collections.Counter(), collections.Counter()
    print('章 | 标题 | 篇数 | verified | corrected | 有摘要')
    for cid in chapter_files(data_dir):
        d = load(data_dir, cid)
        ps = d['papers']
        ver = sum(1 for p in ps if p.get('verification') == 'verified')
        cor = sum(1 for p in ps if p.get('verification') == 'corrected')
        ab = sum(1 for p in ps if p.get('abstract'))
        print(f"{cid} | {d.get('chapter_title','')} | {len(ps)} | {ver} | {cor} | {ab}")
        for p in ps:
            dois[p.get('doi')].add(cid)
            kinds[p.get('kind')] += 1
            if isinstance(p.get('year'), int):
                decades[p['year'] // 10 * 10] += 1
            rows.append((cid, p))
    print(f"\n条目 {len(rows)}；唯一 DOI {len(dois)}；跨章共享 DOI {sum(1 for v in dois.values() if len(v) > 1)}")
    print('类型：' + ', '.join(f'{k} {v}' for k, v in kinds.most_common()))
    print('年代：' + ', '.join(f'{k}s {v}' for k, v in sorted(decades.items())))
    print('\n必读候选（每章按 重要性>被引>年份 取前 6）：')
    seen = set()
    for cid in chapter_files(data_dir):
        ps = sorted(load(data_dir, cid)['papers'], key=sort_key)
        k = 0
        for p in ps:
            if p['doi'] in seen:
                continue
            seen.add(p['doi'])
            k += 1
            print(f"{cid} | {cite(p)} | {(p.get('journal') or '')[:30]} | imp{p.get('importance')} | cit{p.get('cited_by_count')} | {(p.get('title') or '')[:90]} | {p['doi']}")
            if k >= 6:
                break


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'digest':
        digest(sys.argv[2], sys.argv[3])
    elif cmd == 'table':
        table(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == 'index':
        index(sys.argv[2])
    elif cmd == 'stats':
        stats(sys.argv[2])
    else:
        sys.exit(__doc__)

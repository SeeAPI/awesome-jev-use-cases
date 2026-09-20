#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate discovery surfaces from casebook narratives and curated JSON."""
import argparse
import json
import re
from catalog import ROOT, LANGUAGES, read_catalog, load_cases, slug, narrative_summary, settings, to_casebook, narrative_field, first_sentence

FEATURED = [
    ('jev-ultrafast', 'Browser automation', '浏览器自动化'),
    ('jev-codex-router', 'Model routing', '模型路由'),
    ('jev-review', 'Code review', '代码审查'),
    ('sift', 'Search reranking', '搜索重排'),
    ('ghrezakh74-jevticktrouter', 'Support ticket triage', '工单分流'),
    ('jev-moderation-bot', 'Community moderation', '社区审核'),
]


def root_links(text):
    return text.replace('(../', '(').replace('src="../', 'src="')


def dumps(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def additional_media(item, lang):
    if not item:
        return ''
    en = lang == 'en'
    if item['kind'] == 'documentation':
        return f"[{'Implementation walkthrough' if en else '实现说明'}：{item['label'][lang]}]({item['source_url']})\n\n"
    return (f'<a href="{item["source_url"]}"><img src="{item["image_url"]}" alt="{item["alt"][lang]}" width="720" /></a>\n\n'
            + item['caption'][lang] + '\n\n'
            + f"[{'Original image' if en else '查看原图'}]({item['source_url']}) · [{'More author screenshots' if en else '更多作者截图'}]({item['gallery_url']}) · [{'License declaration' if en else '许可声明'}]({item['license_url']})\n\n")


def build():
    localized, catalog = read_catalog()
    cases = load_cases()
    by_id = {r['id']: r for r in cases}
    by_catalog_id = {r['id']: r for r in catalog}
    config = settings()
    media_sources = json.loads((ROOT / 'data/featured-media.json').read_text())
    outputs = {'data/cases.json': dumps(cases), 'data/catalog.json': dumps(catalog)}
    for r in cases:
        idx = by_catalog_id[r['id']]
        tested = "yes" if r["evidence"]["verified_by_seeapi"] else "no"
        text = f"# {r['title']['en']}\n\n[Read the full case](../{idx['details']['en']}) · [阅读完整案例](../{idx['details']['zh']})\n\nMetadata reference; the Casebook is the main reading entry.\n\n{r['summary']['en']}\n\n"
        text += f"**Evidence:** `{r['evidence']['level']}` · **Reviewed:** {r['evidence']['reviewed_at']} · **Live-tested by SeeAPI:** {tested}\n\n"
        text += f"**Primitive:** {', '.join(r['jev_primitive'])} · **Action:** {', '.join(r['software_action'])}\n\n"
        text += f"[Original source]({r['source_url']}) · [Full case](../{idx['details']['en']}) · [Data record](../data/cases/{r['id']}.json)\n\n"
        text += '## Limits\n\n' + '\n'.join('- ' + x for x in r['limitations']['en']) + '\n\n'
        text += f"## 中文\n\n{r['summary']['zh']}\n\n" + '\n'.join('- '+x for x in r['limitations']['zh'])
        text += f"\n\n[完整中文案例](../{idx['details']['zh']}) · [证据说明](../docs/evidence.md)\n"
        if r['recipe_ids']:
            text += '\n## Recipe\n\n' + '\n'.join(f'- [{recipe}](../recipes/{recipe}.md)' for recipe in r['recipe_ids']) + '\n'
        outputs['cases/' + r['id'] + '.md'] = text
    for lang in ['en','zh']:
        en = lang == 'en'
        rows = localized[lang]
        title = '# Awesome Jev Use Cases\n\n'
        language = '[English](README.md) · [简体中文](README.zh-CN.md)\n\n'
        intro = ('Discover public projects using **Jev** for automation, model routing, search and business decisions. See what Jev judges, how software uses the answer, and what you can reuse. Use the **[Jev solution finder Skill](#find-your-solution-with-the-skill)** to find relevant cases and plan your implementation.\n\n' if en else '收集 **Jev** 在自动化、模型路由、搜索和业务判断中的公开案例，说明 Jev 判断什么、程序如何使用结果，以及哪些做法值得借鉴。也可以用配套的 **[Jev solution finder Skill](#用-skill-找到你的实现方案)**，让 Agent 帮你找案例、比较方案。\n\n')
        banner = '<img src="assets/banner.png" alt="Awesome Jev Use Cases — curated by SeeAPI" width="720" />\n\n'
        stats = f"**{len(catalog)} {'cases · Content updated' if en else '个案例 · 内容更新'}: {config['updated_at']}**\n\n"
        nav = ('**[Use the Skill](#find-your-solution-with-the-skill) · [Browse cases](#browse-by-use-case) · [Featured cases](#featured-cases) · [Build with these cases](#build-with-these-cases) · [Suggest a case](CONTRIBUTING.md)**\n\n' if en else '**[使用 Skill](#用-skill-找到你的实现方案) · [分类目录](#按场景浏览) · [精选案例](#精选案例) · [开始实践](#从案例到自己的实现) · [推荐案例](CONTRIBUTING.md)**\n\n')
        credit = ('Curated by [SeeAPI](https://github.com/SeeAPI), independently of TypeSafe. Cases link to original work; author results are not our measurements.\n\n' if en else '由 [SeeAPI](https://github.com/SeeAPI) 独立整理，非 TypeSafe 官方项目。案例链接原作者作品，作者结果不等于本仓库实测。\n\n')
        skill_intro = (
            '## Find your solution with the Skill\n\n'
            '**Describe your task; let your agent find relevant Jev projects, compare their approaches and limits, and draft a workflow with source links.**\n\n'
            'With this repository available in your agent’s workspace, copy this request:\n\n'
            '> Read this repository’s SKILL.md. I want to route support tickets. Find 3 relevant cases, compare what Jev judges and what application code does, then propose a minimal workflow with a human-review path. Cite the original projects and distinguish documented behavior from tested results.\n\n'
            '[Get started / install](docs/skill.md) · [Read the Skill](SKILL.md)\n\n'
            if en else
            '## 用 Skill 找到你的实现方案\n\n'
            '**描述你的需求，让 Agent 帮你查找相关 Jev 项目、比较做法与边界，并生成带来源链接的工作流草案。**\n\n'
            '将本仓库放入 Agent 工作目录后，直接复制这段需求：\n\n'
            '> 读取本仓库的 SKILL.md。我想做客服工单分流，请找出 3 个相关案例，比较 Jev 判断什么、业务代码负责什么，再给出带人工复核路径的最小实现方案。附上原始项目链接，并区分文档描述与实测结果。\n\n'
            '[使用与安装指南](docs/skill.md) · [查看 Skill 定义](SKILL.md)\n\n'
        )
        featured = '## ' + ('Featured cases' if en else '精选案例') + '\n\n'
        rows_by_id = {r['id']: r for r in rows}
        for id,label,zlabel in FEATURED:
            record = by_id.get(id)
            row = rows_by_id[id]
            featured += f"### {label if en else zlabel} · {row['title']}\n\n"
            featured += root_links(narrative_summary(row)) + '\n\n'
            if record:
                primitives = ', '.join(x.title() for x in record['jev_primitive'])
                limit = record['limitations'][lang][0]
            else:
                # The documented ticket example uses all three; no new test claim.
                primitives = 'Choice, Score, Noul'
                limit = re.search(r'^\*\*(?:Scope|边界)[：:]?\*\*[：:]?\s*(.+)$', row['body'], re.M)[1]
            takeaway = narrative_field(row, ['Pattern', '可借鉴点', '实现模式'])
            if id == 'sift':
                takeaway = ('Keep relevance judgments separate from ranking rules; users can restore the original order.' if en else '将相关性判断与排序规则分离，并让用户能够恢复原始顺序。')
            if takeaway:
                featured += ('**Reusable pattern:** ' if en else '**可借鉴点：** ') + root_links(takeaway) + '\n\n'
            featured += ('**Jev primitives:** ' if en else '**Jev 判断类型：** ') + primitives + '\n\n'
            featured += ('**Scope:** ' if en else '**适用边界：** ') + limit + '\n\n'
            featured += f"[{'Source' if en else '项目来源'}]({row['source_url']}) · [{'Full case' if en else '案例详情'}]({LANGUAGES[lang]}#{row['anchor']})"
            if record and record['recipe_ids']:
                featured += f" · [{'Try the recipe' if en else '查看工作流配方'}](recipes/model-routing{'' if en else '.zh-CN'}.md)"
            featured += '\n\n'
            if id in ('jev-ultrafast', 'jev-review'):
                media = re.search(r'(<img [^>]+>\s*\n\s*[^\n]+)', row['body'])
                if not media:
                    raise ValueError('Missing featured media: ' + id)
                featured += root_links(media[1]) + '\n\n'
            featured += additional_media(media_sources.get(id), lang)
        directory = '## ' + ('Browse by use case' if en else '按场景浏览') + '\n\n'
        directory += ('| Category | Cases | What you can find |\n| --- | ---: | --- |\n' if en else '| 分类 | 案例数 | 可以找到什么 |\n| --- | ---: | --- |\n')
        category_names = [c['title'][lang] for c in config['categories']]
        for category in config['categories']:
            name = category['title'][lang]
            count = sum(r['category'] == category['id'] for r in rows)
            directory += f"| [{name}](#{slug(name)}) | {count} | {category['description'][lang]} |\n"
        directory += '\n'
        browse = ('## All cases\n\nPurpose summaries and original sources for every project. Open a case for its implementation and limits.\n\n' if en else '## 全部案例\n\n每个项目保留用途摘要和原始来源，点击详情查看实现与边界。\n\n')
        featured = featured.replace('\n\n', ('\n\nA selection across different tasks; placement is not a performance ranking.\n\n' if en else '\n\n覆盖不同任务的编辑精选，不代表性能排名。\n\n'), 1)
        used = set([slug('Awesome Jev Use Cases'),slug('Browse by use case' if en else '按场景浏览'),slug('Featured cases' if en else '精选案例')])
        for category in category_names:
            used.add(slug(category))
            browse += f'## {category}\n\n'
            for r in rows:
                if r['category_title'] != category:
                    continue
                aliases = list(dict.fromkeys([r['anchor']] + r['aliases']))
                used.update(aliases)
                anchors = ''.join(f'<a id="{a}"></a>' for a in aliases)
                summary = narrative_summary(r)
                browse += f"{anchors}\n\n**{r['title']}** — {root_links(summary)}<br>\n"
                takeaway = narrative_field(r, ['Pattern', '可借鉴点', '实现模式'])
                scope = first_sentence(narrative_field(r, ['Scope', '边界']))
                if takeaway:
                    browse += ('**Reusable pattern:** ' if en else '**可借鉴点：** ') + root_links(takeaway) + '<br>\n'
                if scope:
                    browse += ('**Key limit:** ' if en else '**关键边界：** ') + root_links(scope) + '<br>\n'
                browse += f"[{'Source' if en else '项目来源'}]({r['source_url']}) · [{'Details & limits' if en else '详情与边界'}]({LANGUAGES[lang]}#{r['anchor']})\n\n"
            browse += '\n'
        bottom = ('## What is Jev?\n\nJev is TypeSafe AI’s System One model for typed judgments. Choice selects candidates, Noul evaluates a yes/no proposition, and Score rates ordered criteria. Application code decides what to do with those answers. [Model background](docs/casebook.md#what-is-jev).\n\n## Model origin & access options\n\nStart with the [official documentation](https://docs.typesafe.ai/introduction) or the [provider and SDK guide](docs/casebook.md#model-origin--access-options). This collection does not assume provider interfaces are interchangeable.\n\n## Evidence & scope\n\nRead [evidence definitions](docs/evidence.md) and the [full review scope](docs/casebook.md#evidence--scope). This release adds offline recipe checks, not independent model benchmark results.\n\n## Sources & contributions\n\n[Suggest or correct a case](CONTRIBUTING.md) · [Source history](docs/casebook.md#sources--contributions) · [Maintenance guide](docs/maintaining.md) · [Changes](CHANGELOG.md).\n\n## License\n\nOriginal documentation: [CC BY 4.0](LICENSE). Code: [MIT](LICENSE-CODE). Third-party materials retain their [own rights and attribution](THIRD_PARTY_NOTICES.md); see [scope](NOTICE.md).\n' if en else '## Jev 是什么？\n\nJev 是 TypeSafe AI 的结构化判断模型：Choice 选择候选，Noul 判断是非命题，Score 按有序标准评分，业务代码决定后续动作。[模型背景](docs/casebook.zh-CN.md#jev-是什么)。\n\n## 模型来源与接入方式\n\n从[官方文档](https://docs.typesafe.ai/introduction)或[供应商与 SDK 指南](docs/casebook.zh-CN.md#模型来源与接入方式)开始，不假设各渠道接口互相兼容。\n\n## 发现来源与更新方式\n\n查看[证据定义](docs/evidence.md)、[原始来源与核查范围](docs/casebook.zh-CN.md#发现来源与更新方式)、[贡献指南](CONTRIBUTING.md)、[维护指南](docs/maintaining.md)和[更新记录](CHANGELOG.md)。本轮增加离线 Recipe 检查，不新增独立模型基准结果。\n\n## 许可证\n\n原创文档采用 [CC BY 4.0](LICENSE)，代码采用 [MIT](LICENSE-CODE)，第三方素材保留[原有权利与署名](THIRD_PARTY_NOTICES.md)，详见[授权范围](NOTICE.md)。\n')
        next_steps = ('## Build with these cases\n\n- [Model-routing recipe](recipes/model-routing.md): adapt a minimal Choice workflow; the default run is offline.\n- [Use the Skill](docs/skill.md): find relevant projects and draft workflows with sources.\n- [Benchmark evidence](benchmarks/README.md): inspect existing studies and their limits.\n\n' if en else '## 从案例到自己的实现\n\n- [模型路由 Recipe](recipes/model-routing.zh-CN.md)：从最小 Choice 工作流开始，默认离线预览。\n- [使用 Skill](docs/skill.md)：查找相关项目、比较方案并生成带来源的工作流。\n- [评测证据](benchmarks/README.md)：了解已有研究及其适用边界。\n\n')
        bottom = next_steps + bottom
        used.update(slug(h) for h in re.findall(r'^## (.+)$',bottom,re.M))
        # Retain old subheading anchors as links to their original full sections.
        old = to_casebook((ROOT / f'content/pages/background.{lang}.md').read_text())
        compatibility = []
        for heading in re.findall(r'^#{1,6} (.+)$',old,re.M):
            anchor = slug(heading)
            if anchor in used:
                continue
            used.add(anchor)
            compatibility.append(f'<a id="{anchor}"></a>[{heading}]({LANGUAGES[lang]}#{anchor})')
        if compatibility:
            bottom += '\n' + ' · '.join(compatibility) + '\n'
        page = '<!-- Generated by scripts/generate.py; edit source records or the generator. -->\n\n' + title + language + intro + banner + stats + nav + credit + skill_intro + directory + featured + browse + bottom
        # Full narratives remain the single reader-facing detail destination.
        home = 'README.md' if en else 'README.zh-CN.md'
        book = '<!-- Generated by scripts/generate.py; edit content/cases/*.md. -->\n\n'
        book += f"[{'← Home' if en else '← 返回首页'}](../{home})\n\n# {'Jev Casebook' if en else 'Jev 完整案例集'}\n\n"
        book += directory
        for category in category_names:
            book += f'## {category}\n\n'
            for row in rows:
                if row['category_title'] != category:
                    continue
                aliases = list(dict.fromkeys([row['anchor']] + row['aliases']))
                book += ''.join(f'<a id="{a}"></a>' for a in aliases) + '\n\n'
                book += f"### {row['number']}. {row['title']}\n\n{row['body']}\n\n"
                if row['id'] in media_sources:
                    book += additional_media(media_sources[row['id']], lang)
        book += old
        outputs[LANGUAGES[lang]] = book
        outputs['README.md' if en else 'README.zh-CN.md'] = page
        if not en:
            outputs['README_zh.md'] = page
    outputs['llms.txt'] = '# Awesome Jev Use Cases\n\n> Case discovery and workflow design; no implied runtime validation.\n\n' + '\n'.join([
        f'- [Full catalog](data/catalog.json): {len(catalog)} stable IDs, bilingual purpose summaries, sources and detail links.',
        f'- [Structured cases](data/cases.json): {len(cases)} curated bilingual records with evidence and limitations.',
        '- [Agent skill](SKILL.md): find, compare and design with citations.',
        '- [Recipes](recipes/README.md): model routing; offline checks only.',
        '- [Evidence](docs/evidence.md): distinguish review, demo, live test and benchmark.',
        '- [Casebook](docs/casebook.md): complete narratives.',
        '- [中文案例集](docs/casebook.zh-CN.md): full Chinese narratives.',
    ]) + '\n'
    return outputs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for name, content in build().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content)
    if stale:
        raise SystemExit('Generated files out of date: ' + ', '.join(stale))
    print('Generated output is current.' if args.check else 'Generated README, catalog, structured cases, case cards and llms.txt.')

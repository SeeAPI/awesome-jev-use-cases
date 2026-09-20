import copy
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from catalog import load_cases, read_catalog, load_entries
from find_cases import search
from validate import check_metadata

class CatalogTests(unittest.TestCase):
    def test_higher_evidence_needs_artifacts(self):
        r=copy.deepcopy(load_cases()[0]);_,catalog=read_catalog()
        r['evidence']['level']='seeapi-tested';r['evidence']['verified_by_seeapi']=True
        self.assertTrue(check_metadata([r],catalog))
        r['evidence']['level']='independently-benchmarked';r['evidence']['report_path']='missing-report.md'
        self.assertTrue(check_metadata([r],catalog))

    def test_index_identity_cannot_drift(self):
        r=copy.deepcopy(load_cases()[0]);_,catalog=read_catalog()
        r['source_url']='https://example.com/wrong-project'
        self.assertTrue(check_metadata([r],catalog))

    def test_english_chinese_and_absent_queries(self):
        self.assertTrue(any('rerank' in x['id'] or x['id']=='sift' for x in search('reranking')))
        self.assertEqual(search('模型路由')[0]['id'],'jev-codex-router')
        self.assertEqual(search('zzzxunmatchedzzz'),[])
        self.assertEqual(search(''),[])

    def test_catalog_only_does_not_invent_evidence(self):
        result=search('gomoku')[0]
        self.assertIsNone(result['evidence'])
        self.assertEqual(result['id'], 'xiechengyuan-jev-gomoku')

class DiscoveryRegressionTests(unittest.TestCase):
    def test_body_keywords_and_bilingual_aliases_find_unstructured_cases(self):
        for query in ('captions', 'subtitles', '字幕', 'YouTube'):
            with self.subTest(query=query):
                matches = search(query, 100)
                match = next(r for r in matches if r['id'] == 'valentynkit-jev-skip')
                self.assertIsNone(match['evidence'])
                self.assertIn('captions', match['summary']['en'])
        self.assertEqual(search('totally-unknown-word-xyz'), [])

    def test_insertions_do_not_change_ids_categories_or_detail_links(self):
        entries = load_entries()
        _, before = read_catalog(entries)
        added = copy.deepcopy(entries[0])
        added.update(id='new-regression-case', source_url='https://example.com/new-case', order=0)
        _, after = read_catalog(entries + [added])
        by_id = {r['id']: r for r in after}
        self.assertTrue(any(r['number'] != by_id[r['id']]['number'] for r in before))
        for row in before:
            for key in ('id', 'category', 'source_url', 'details'):
                self.assertEqual(row[key], by_id[row['id']][key])
        self.assertEqual(check_metadata(load_cases(), after), [])

    def test_category_reordering_does_not_reassign_membership(self):
        from unittest.mock import patch
        from catalog import settings
        config = settings()
        entries = load_entries()
        _, before = read_catalog(entries)
        config['categories'].reverse()
        with patch('catalog.settings', return_value=config):
            _, after = read_catalog(entries)
        self.assertEqual({r['id']: r['category'] for r in before},
                         {r['id']: r['category'] for r in after})

    def test_both_homepages_keep_directory_before_featured(self):
        from generate import build
        pages = build()
        for path, toc, featured, cases in (
            ('README.md', '## Browse by use case', '## Featured cases', '## All cases'),
            ('README.zh-CN.md', '## 按场景浏览', '## 精选案例', '## 全部案例')):
            text = pages[path]
            self.assertLess(text.index(toc), text.index(featured))
            self.assertLess(text.index(featured), text.index(cases))
            self.assertEqual(text.count(toc), 1)
            for row in read_catalog()[1]:
                self.assertIn('id="case-' + row['id'] + '"', text)

if __name__=='__main__':unittest.main()

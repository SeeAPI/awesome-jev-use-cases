import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('routing',ROOT/'recipes/model-routing/run.py')
routing=importlib.util.module_from_spec(spec);spec.loader.exec_module(routing)

class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.response=json.loads((ROOT/'recipes/model-routing/response.fixture.json').read_text())

    def test_valid_tiers_and_confidence_boundary(self):
        for tier in ['fast','strong']:
            answer=self.response['answers']['route'];answer['choice']=tier;answer['confidence']=0.8
            self.assertEqual(routing.decide(self.response,0.8)['tier'],tier)
        answer['confidence']=0.7999
        self.assertEqual(routing.decide(self.response,0.8)['action'],'review')

    def test_missing_malformed_and_nonfinite_answers_review(self):
        for bad in [None,[],{}, {'answers':None}, {'answers':{'route':[]}}]:
            self.assertEqual(routing.decide(bad,0.8)['action'],'review')
        for key,value in [('choice','attacker'),('confidence',True),('confidence',float('nan')),('confidence',-1),('type','noul'),('probabilities',{'fast':0.1,'strong':0.1}),('probabilities',{'fast':True,'strong':0})]:
            candidate=copy.deepcopy(self.response);candidate['answers']['route'][key]=value
            self.assertEqual(routing.decide(candidate,0.8)['action'],'review')

    def test_default_and_fixture_never_open_network(self):
        with patch('urllib.request.build_opener',side_effect=AssertionError('network forbidden')):
            with patch('builtins.print'):
                self.assertEqual(routing.main([]),0)
                self.assertEqual(routing.main(['--response',str(ROOT/'recipes/model-routing/response.fixture.json')]),0)

    def test_network_failure_returns_review(self):
        with patch.dict('os.environ',{'TYPESAFE_API_KEY':'dummy-test-only'}):
            with patch('urllib.request.build_opener') as opener, patch('builtins.print') as output:
                opener.return_value.open.side_effect=TimeoutError()
                self.assertEqual(routing.main(['--live']),1)
                value=json.loads(output.call_args[0][0])
                self.assertEqual(value['decision']['action'],'review')
                self.assertNotIn('dummy-test-only',json.dumps(value))

    def test_cli_fixture_labels_synthetic(self):
        result=subprocess.check_output([sys.executable,str(ROOT/'recipes/model-routing/run.py'),'--response',str(ROOT/'recipes/model-routing/response.fixture.json')],text=True)
        self.assertTrue(json.loads(result)['synthetic'])

if __name__=='__main__':unittest.main()

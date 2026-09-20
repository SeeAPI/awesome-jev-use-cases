#!/usr/bin/env python3
"""Build a portable local skill folder without installing it in any agent."""
import argparse
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]

FILES = ['SKILL.md','llms.txt','README.md','README.zh-CN.md','README_zh.md','CONTRIBUTING.md','CHANGELOG.md','NOTICE.md','THIRD_PARTY_NOTICES.md','LICENSE','LICENSE-CODE','requirements-dev.txt','CITATION.cff']
DIRS = ['content','data','cases','docs','recipes','benchmarks','assets','scripts','tests']

def package(output):
    output=Path(output).resolve()
    if output.exists():
        raise ValueError('Use a new output directory; existing folders are never overwritten')
    if output==ROOT or ROOT in output.parents:
        raise ValueError('Choose an output directory outside the repository')
    output.mkdir(parents=True)
    for name in FILES:
        shutil.copy2(ROOT/name,output/name)
    for name in DIRS:
        shutil.copytree(ROOT/name,output/name,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    try:
        print(package(args.output))
    except ValueError as error:
        parser.error(str(error))

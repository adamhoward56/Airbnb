#!/usr/bin/env python

from json import load
from sys import argv

def loc(nb):
    cells = load(open(nb))['cells']
    #for c in cells:
    #    if c['cell_type'] == 'markdown': print(c['source'])
    return sum(sum(len(line.split()) for line in c['source']) for c in cells if c['cell_type'] == 'markdown')

def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)

if __name__ == '__main__':
    print(run(argv[1:]))

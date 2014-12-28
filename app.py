#!/usr/bin/env python2.7

import sys, getopt
from docxstache.docxstache import docxstache

import json

d = json.load(open(sys.argv[2]))

docxstache(sys.argv[1], d, sys.argv[3])

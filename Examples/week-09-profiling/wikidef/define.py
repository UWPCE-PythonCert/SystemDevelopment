#!/usr/bin/env python

import sys

from definitions import Definitions
from html2text import html2text

title = sys.argv[1]

definition = Definitions.article(title)
txt = html2text(definition)
print txt.encode('utf-8')


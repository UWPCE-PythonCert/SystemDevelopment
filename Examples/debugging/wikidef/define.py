#!/usr/bin/env python

import sys

from definitions import Definitions
from html2text import html2text

title = len(sys.argv) == 2 and sys.argv[1] or ""

definition = Definitions.article(title)
txt = html2text(definition)
print txt.encode('utf-8')


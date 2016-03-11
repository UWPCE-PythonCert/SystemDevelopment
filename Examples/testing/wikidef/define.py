#!/usr/bin/env python

import sys

from definitions import Definitions

title = sys.argv[1]

print Definitions.article(title).encode('utf-8')


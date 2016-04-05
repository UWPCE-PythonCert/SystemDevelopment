#!/usr/bin/env python3

"""
Script to contact Wikipedia and get articles on a specified topic.
python define.py interesting_topic
"""

import sys

from definitions import Definitions

title = sys.argv[1]

print(Definitions.article(title).encode('utf-8'))

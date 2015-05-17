#!/usr/bin/env python

from timer import timer

list_data = [l.strip() for l in open('/usr/share/dict/words')] * 10

set_data = set(list_data)


@timer
def set_contains(x):
    return x in set_data

@timer
def list_contains(x):
    return x in list_data
    

if __name__ == "__main__":
    set_contains("zebra")
    list_contains("zebra")

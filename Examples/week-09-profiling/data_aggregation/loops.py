#!/usr/bin/env python

from timer import timer

data = [l.strip() for l in open('/usr/share/dict/words')] * 10

# data contains a list of words.  uppercase all elements two ways:

@timer
def slow():
    upper = []
    for word in data:
        upper.append(word.upper())
    return upper

@timer
def fast_list_comprehension():
    return [x.upper() for x in data]

@timer
def fast_map():
    return map(str.upper, data)

@timer
def fast_generator():
    # super fast.  but is it doing the same work? 
    return (x.upper() for x in data)

if __name__ == "__main__":
    slow()
    fast_map()
    fast_list_comprehension()
    fast_generator()

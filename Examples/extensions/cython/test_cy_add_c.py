#!/usr/bin/env python

"""
simple test code for cy_add1

can be run by itself, or with nose or pytest
"""

import cy_add_c


def test_1():
    assert cy_add_c.add(3, 4) == 7

def test_2():
    assert cy_add_c.add(5, 6) == 11

def test_error():
    """
    you should get an TypeError if you try to add something other than numbers
    """
    try:
        print cy_add_c.add('this', 5)
        assert False # shouldn't get here!
    except TypeError:
        # should have gotten an exception
        pass

if __name__ == "__main__":
    test_1()
    test_2()
    test_error()

    print "if you didn't get an assertion, it worked"




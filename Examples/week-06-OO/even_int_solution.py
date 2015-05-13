#!/usr/bin/env python

"""
Using new to create an always-positive even integer

rounds the input to the nearest even integer.

will even convert a string to an int...

"""

##subclassing an int
class EvenInt(int):
    """
    An integer that is always even
    """
    def __new__(cls, val):
        val = round(float(val) / 2) * 2
        return int.__new__(cls, val)


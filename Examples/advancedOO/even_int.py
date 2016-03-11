#!/usr/bin/env python

"""
Using new to create an even integer

rounds the input to the nearest even integer.

will even convert a string to an int...

"""


class EvenInt(int):
    """
    An integer that is always even
    """

    def __new__(cls, input):
        input = float(input)
        i = int(round(input / 2) * 2)
        return int.__new__(cls, i)

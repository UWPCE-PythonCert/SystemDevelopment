#!/usr/bin/env python

"""
example of __new__
"""


# the general case:
class Test():
    def __new__(cls, arg):
        print("in __new__:")
        print(arg)
        obj = super().__new__(cls)
        # you _could_ do something with arg here:
        obj.arg = arg
        # but it's usally better to save that for the __init__
        return obj

    def __init__(self, arg):
        print("in __init__")
        print(arg)
        self.that = arg


# subclassing a string

class CapitalString(str):
    """
    A string class that is always capitalized...
    """
    def __new__(cls, in_string):
        print("in CapitalString.__new__")
        print(cls)
        # return str.__new__(cls, in_string.title())
        return super().__new__(cls, in_string.title())

if __name__ == "__main__":
    print(CapitalString("this is a string"))

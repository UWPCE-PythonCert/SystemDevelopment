#!/usr/bin/env python

"""
example of __new__
"""



## the general case:
class Test(object):
    def __new__(cls, arg):
        print "in __new__", 
        print arg
        obj =  object.__new__(cls, arg)
        obj.this = arg # but you probably don't want to do this!
        return obj

    def __init__(self, arg):
        print "in __init__", 
        print arg
        self.that = arg


##subclassing a string

class CapitalString(str):
    """
    A string class that is always capitalized...
    """
    def __new__(cls, in_string):
        print "in CapitalString.__new__"
        return str.__new__(cls, in_string.title() )

# try it:
if __name__ == "__main__":
    print CapitalString("this is a string")





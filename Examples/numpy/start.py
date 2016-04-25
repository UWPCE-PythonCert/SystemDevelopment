#!/usr/bin/env python

"""
script to start up demo for numpy talk

just the one unility at this point..
"""


def print_info(a, name="arr"):
    print(name, ":")
    print(a)
    print("%s.shape:" % name, a.shape)
    print("%s.dtype:" % name, a.dtype)
    print("%s.itemsize" % name, a.itemsize)
    print("%s.ndim:" % name, a.ndim)
    print("%s.strides" % name, a.strides)
    print("%s.flags:\n" % name, a.flags)

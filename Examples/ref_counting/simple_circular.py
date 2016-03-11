#!/usr/bin/env python

"""
Simple contrived example of circular reference counting
"""

import sys

l1 = [1,]
l2 = [2,]

l1_id = id(l1)
l2_id = id(l2)

print "initial ref counts:"
print "l1:", sys.getrefcount(l1)
print "l2:", sys.getrefcount(l2)

print "now add the circular references:"
l1.append(l2)
l2.append(l1)

print "ref counts after the circular reference is added"
print "l1:", l1, "refcount:", sys.getrefcount(l1)
print "l2:", l2, "refcount:", sys.getrefcount(l2)

print "delete one"
del l1
print "l2:", sys.getrefcount(l2)

print "delete the other"
del l2

print "but are they still there???"






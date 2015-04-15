#!/usr/bin/env python

"""
Simple contrived example of circular reference counting

This one does some testing with di.ref_by_id
"""

import sys
import di
import gc

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
print "l1:", sys.getrefcount(l1)
print "l2:", sys.getrefcount(l2)

print "delete one"
del l1
print "l1:", sys.getrefcount(l2)

print "delete the other"
del l2

print "are they still there?"
print "l1's refcount:", di.ref_by_id(l1_id)
print "l2's refcount:", di.ref_by_id(l2_id)
print "-- yes they are!"

print "now run the garbage collector"
print "It collected:", gc.collect(), "objects"

print "ref counts now???"
print "l1's refcount:", di.ref_by_id(l1_id)
print "l2's refcount:", di.ref_by_id(l2_id)

print "yup -- they'll get cleaned up"





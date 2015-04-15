#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
a simple test of a circular reference that gc.collect() will not clean up.

And watch the memory grow!

"""


import sys
import gc
import weakref

import mem_check


class MyChild(object):
    def __init__(self, parent):
        #self.parent = parent
        # if a weak ref is used, then no memory leak.
        self.parent = weakref.proxy(parent)

        ## store some data so it will use appreciable memory
        ## multiply by 1234 to reduce interning
        self.data = [1234*i for i in range(100000)]

    def __del__(self):
        """ __del__ defined to defeat GC"""
        print 'MyChild deleted', id(self)


class MyParent(object):
    def __init__(self):
        self.children = []
    def addChild(self):
        child = MyChild(self)
        self.children.append(child)
        return child
    def __del__(self):
        """ __del__ defined to defeat GC"""
        print 'MyParent deleted', id(self)


if __name__ == "__main__":

    # create a bunch in a loop:
    for i in range(50):
        print "iteration:", i
        p = MyParent()
        p.addChild()
        p.addChild()
        p.addChild()
        print "ref count:", sys.getrefcount(p)
        print "mem_use: %f MB"%mem_check.get_mem_use()
        del p
        print "collected", gc.collect()

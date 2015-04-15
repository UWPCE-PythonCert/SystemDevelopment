#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import weakref
import gc

deleted_object_messages = []


class MyChild(object):
    def __init__(self, parent):
        self.parent = parent
        #self.parent = weakref.ref(parent)
        #self.parent = weakref.proxy(parent)

        ## store some data so it will use appreciable memory
        ## multiply by 1234 to avoid interning
        self.data = [1234*i for i in range(100000)]

    def __del__(self):
        deleted_object_messages.append( ('MyChild deleted', id(self)) )


class MyParent(object):
    def __init__(self):
        self.children = []
    def addChild(self):
        child = MyChild(self)
        self.children.append(child)
        return child
    def __del__(self):
        deleted_object_messages.append( ('MyParent deleted', id(self)) )

if __name__ == "__main__":

    p = MyParent()

    print "refcount for p:", sys.getrefcount(p)
    assert sys.getrefcount(p) == 2

    a = p.addChild()
    a2 = p.addChild()
    print "refcount for p after adding an two children:", sys.getrefcount(p)
    assert sys.getrefcount(p) == 2

    print "p's children:", p.children
    assert len(p.children) == 2

    print " a is:", a
    print "a's parent:", a.parent
    print "a's parent's children:", a.parent.children

    assert a is a.parent.children[0]
    assert a2 is a.parent.children[1]


    print "a's refcount:", sys.getrefcount(a)
    assert sys.getrefcount(a) == 3

    print "a2's refcount:", sys.getrefcount(a2)
    assert sys.getrefcount(a2) == 3

    del p
    print "after deleting p:"

    print "a's refcount:", sys.getrefcount(a)
    assert sys.getrefcount(a) == 2

    print "a2's refcount:", sys.getrefcount(a2)
    assert sys.getrefcount(a2) == 2

    print "deleting a:"
    id_a = id(a)
    del a
    print deleted_object_messages
    assert deleted_object_messages[-1][0] == 'MyChild deleted'
    assert deleted_object_messages[-1][1] == id_a

    print "deleting a2:"
    id_a2 = id(a2)
    del a2
    print deleted_object_messages
    assert deleted_object_messages[-1][0] == 'MyChild deleted'
    assert deleted_object_messages[-1][1] == id_a2





#!/usr/bin/env python

class NameMangler(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
                uppercase_attr[name] = val
            else:
                uppercase_attr[name] = val

        return super(NameMangler, cls).__new__(cls, clsname, bases, uppercase_attr)

class Foo(object):
    __metaclass__ = NameMangler
    x = 1

if __name__ == "__main__":
    f = Foo()
    print f.x
    print f.X

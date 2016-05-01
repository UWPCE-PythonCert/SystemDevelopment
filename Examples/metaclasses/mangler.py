#!/usr/bin/env python3


class NameMangler(type):

    def __new__(cls, clsname, bases, _dict):
        uppercase_attr = {}
        for name, val in _dict.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
                uppercase_attr[name] = val
            else:
                uppercase_attr[name] = val

        return super().__new__(cls, clsname, bases, uppercase_attr)


class Foo(metaclass=NameMangler):
    x = 1


if __name__ == "__main__":
    f = Foo()
    print(f.x)
    print(f.X)

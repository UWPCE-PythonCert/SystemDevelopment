class A(object):
    def do_your_stuff(self):
        print("doing A's stuff")


class B(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing B's stuff")


class C(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing C's stuff")


class D(B, C):
    def do_your_stuff(self):
        B.do_your_stuff(self)
        C.do_your_stuff(self)
        print("doing D's stuff")


if __name__ == '__main__':
    a = A()
    print("\ncalling A's method")
    a.do_your_stuff()

    print("\ncalling B's method")
    b = B()
    b.do_your_stuff()

    print("\ncalling C's method")
    c = C()
    c.do_your_stuff()

    print("\ncalling D's method")
    d = D()
    d.do_your_stuff()

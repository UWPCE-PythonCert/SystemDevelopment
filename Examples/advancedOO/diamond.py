class A(object):
    def do_your_stuff(self):
        print "doing A's stuff"
    
class B(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print "doing B's stuff"
    
class C(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print "doing C's stuff"

class D(B,C):    
    def do_your_stuff(self):
        B.do_your_stuff(self)
        C.do_your_stuff(self)
        print "doing D's stuff"


if __name__ == '__main__':
    a = A()
    a.do_your_stuff()

    print
    b = B()
    b.do_your_stuff()

    print
    c = C()
    c.do_your_stuff()

    print 
    d = D()
    d.do_your_stuff()


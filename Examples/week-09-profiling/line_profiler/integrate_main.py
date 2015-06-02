#!/usr/bin/env python

# from integrate import integrate_f_with_functional_tools as integrate_f
from integrate import integrate, f

a = 0.0
b = 10.0

@profile
def test():
    for N in (10**i for i in xrange(1,6)):
        print "Numerical solution with N=%(N)d : %(x)f" % \
            {'N': N, 'x': integrate(f, a, b, N)}

if __name__ == "__main__":
    test()
    

#!/usr/bin/env python

from integrate import f, integrate as _integrate
from decorators import timer

@timer
def integrate(*args):
    return _integrate(*args)

a = 0.0
b = 10.0

for N in (10**i for i in xrange(1,8)):
    print "Numerical solution with N=%(N)d : %(x)f" % \
        {'N': N, 'x': integrate(f, a, b, N)}

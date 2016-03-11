#!/usr/bin/env python

# a cython version with no changes -- pure python!

import cython

cdef double f(double x):
    """simple objective function to integrate"""

    return x**2.0 - x

@cython.cdivision(True)
def double integrate_f(double a, double b, int N):
    """
    integrates the function:

    f(x) = x**2 - x

    from a to b, using N steps, using the simple rectangle rule approach.
    """

    cdef double s = 0.0
    cdef double dx = 0.0
    cdef int i = 0

    dx = (b - a) / N

    for i in range(N):
        s += f(a + i * dx)
    return s * dx

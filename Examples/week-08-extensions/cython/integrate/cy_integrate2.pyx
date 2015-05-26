#!/usr/bin/env python

# a cython version with some static typing


# The objective function is only called from within Cython,
# so we can make it a cdef function:

cdef f(x):
    """simple objective function to integrate"""
    return x**2-x

def integrate_f(a, b, N):
    """
    integrates the function:

    f(x) = x**2 - x

    from a to b, using N steps, using the simple recatngle rule approach.
    """

    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx



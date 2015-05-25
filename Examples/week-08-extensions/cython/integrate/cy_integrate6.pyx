#!/usr/bin/env python

# a cython version with some static typing


# The objective function is only called from within Cython,
# so we can make it a cdef function:

# but a non-typed cdef isn't any faster -- so add the type defs:

cdef double f(double x):
    """simple objective function to integrate"""
    return x**2 - x

# But this function isn't typed, so it still needs
# to convert py_objects to/from the f()
# so add some more type definitions:

# type everythign passed in to the funciton,
# should be pure C speed from there:

# not much help -- what did we miss?
#  check out the annotated version:
#  cython -a cy_integrate5.pyx
#     still a lot of yellow in that loop!
#
#  oops! didn't type def the counter, i!

def integrate_f(double a, double b, int N):
    """
    integrates the function:

    f(x) = x**2 - x

    from a to b, using N steps, using the simple recatngle rule approach.
    """ 
    cdef double s, dx
    cdef int i

    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a + i*dx)
    return s * dx



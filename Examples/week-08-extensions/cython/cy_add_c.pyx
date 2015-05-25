# distutils: sources = add.c

"""
Cython implementation of the add.c example

This one calls an actual C function to do the work

creates a cython function to call the C function.

"""


# telling cython what the function we want to call looks like.
cdef extern from "add.h":
    # pull in C add function, renaming to c_add for Cython
    int c_add "add" (int x, int y)


def add(x, y):
    return c_add(x, y)









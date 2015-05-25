#!/usr/bin/env python

from ctypes import *

libc = CDLL("libc.dylib")

TenInts = c_int * 10
data = TenInts(*range(10,0,-1))

# http://www.gnu.org/software/libc/manual/html_node/Array-Sort-Function.html
# void qsort (void *array, size_t count, size_t size, comparison_fn_t compare)

# http://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

def py_cmp_func(a, b):
    # print "py_cmp_func", a[0], b[0]
    return a[0] - b[0]

for i in data:
    print i

libc.qsort(data, len(data), sizeof(c_int), CMPFUNC(py_cmp_func))

for i in data:
    print i

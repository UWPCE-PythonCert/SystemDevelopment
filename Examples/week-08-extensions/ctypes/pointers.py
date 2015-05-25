#!/usr/bin/env python

from ctypes import *

libc = CDLL("libc.dylib")

i = c_int()
f = c_float()
s = create_string_buffer('\000' * 32)
print i.value, f.value, repr(s.value)
libc.sscanf("1 3.14 Hello", "%d %f %s",byref(i), byref(f), s)
print i.value, f.value, repr(s.value)

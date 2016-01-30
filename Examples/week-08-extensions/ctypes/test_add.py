#!/usr/bin/env python

import sys

lib_ext = ('.so' if ('darwin' in sys.platform or
                    'linux' in sys.platform)
                else ".dll")

import ctypes
import ctypes.util

# # now load our own shared library
# add = ctypes.cdll.LoadLibrary("add"+lib_ext)

# print "This should be 7:",
# print add.add(3,4)

# Using an already-loaded shared library:
## loading libc and libm (math)
if 'darwin' in sys.platform:
    # OS-X likes full paths...
    libc_name = ctypes.util.find_library("libc")
    libm_name = ctypes.util.find_library("libm")
    print libc_name
    libc = ctypes.CDLL(libc_name)
    libm = ctypes.CDLL(libm_name)
elif 'linux' in sys.platform:
    # linux uses the shared lib search path
#    libc = ctypes.CDLL("libc.so")
    libc = ctypes.util.find_library("libc")
    libc = ctypes.CDLL("/lib/x86_64-linux-gnu/libc.so.6")
    libm = ctypes.CDLL("/lib/x86_64-linux-gnu/libm.so.6")
elif 'win' in sys.platform:
    # Windows can find already loaded dlls by name
    libc = ctypes.cdll.msvcrt # lib c and libm are in msvcrt
    libm = ctypes.cdll.msvcrt

libc.printf("printed via libc printf()\n")

print "passing different types to printf:"
#libc.printf("An int %d, a double %f\n", 1234, 3.14)
libc.printf("An int %d, a double %f\n", 1234, ctypes.c_double(3.14))
#libc.printf("An int %d, a double %f\n", 1234)


## Calling libm
## prototype for pow():
## double pow ( double x, double y )

print "This should be 81.0:",
print libm.pow(ctypes.c_double(3), ctypes.c_double(4))

## need to set the return type!
libm.pow.restype = ctypes.c_double
print "This should be 81.0:",
print libm.pow(ctypes.c_double(3), ctypes.c_double(4))

## if you are going to call the same function a lot,
## you can specify the arument types:

libm.pow.restype = ctypes.c_double
libm.pow.argtypes = [ctypes.c_double, ctypes.c_double]
print "This should be 81.0:",
print libm.pow(3, 4.0)

## much easier!









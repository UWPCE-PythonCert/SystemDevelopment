Automatic Gain Control Example
==============================

Automatic Gain Control is a signal processing procedure:

http://seismicreflections.globeclaritas.com/2013/04/agc-equaliser.html

This is an example of using fortran, C, and Cython to produce a fast AGC
filter for Python/numpy.

Thanks for the folks at IRIS (http://www.iris.edu) for this example and
the Fortran code.

Using these examples:
=====================

The c and cython versions should be usable with any pyton set up to
compile extensions. They use setuptools to call the compiler.

The Fortran / f2c version requires a compatible Fortran compiler. g77
should work fine, but getting a compatible build on anything but Linux
is a trick, and out of scope for this README (sorry). Google for it --
you should find what you need.




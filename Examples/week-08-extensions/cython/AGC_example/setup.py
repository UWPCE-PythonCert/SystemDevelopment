#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

import numpy

cy = Extension("agc_cython",
	           ["agc_cython.pyx",],
		       include_dirs = [numpy.get_include(),],
		       )
c_wrap = Extension("agc_c_cy",
	               ["agc_c_cy.pyx", "agc_c.c"],
	               include_dirs = [numpy.get_include(),],
	               )

setup(
    # ext_modules = [cythonize("agc_cython.pyx"),
    #                cythonize([c_wrap]),
    #               ]
    ext_modules = cythonize( [cy, c_wrap] ),
)


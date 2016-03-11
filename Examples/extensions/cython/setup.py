#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize

setup(name="cython_example",
      ext_modules=cythonize(['cy_add_c.pyx',
                             'cy_add1.pyx',
                             'cy_add2.pyx',
                             ])

      )

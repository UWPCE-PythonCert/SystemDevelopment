#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize

setup(name="cython_example",
      ext_modules=cythonize(['cy_integrate1.pyx',
                             'cy_integrate2.pyx',
                             'cy_integrate3.pyx',
                             'cy_integrate4.pyx',
                             'cy_integrate5.pyx',
                             'cy_integrate6.pyx',
                             'cy_integrate7.pyx',
                             ])
      )

#!/usr/bin/env python

from distutils.core import setup, Extension

setup(
    name='Cdiv',
    version='1.0',
    description='sample method that does exceptions',
    ext_modules=[Extension('divide', sources=['divide.c'])],
)


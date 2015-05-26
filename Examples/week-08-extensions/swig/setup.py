#!/usr/bin/env python

from setuptools import setup, Extension

setup(
    name='add',
    py_modules=['add'],
    ext_modules=[
        Extension('_add', sources=['add.c', 'add.i'])
    ]
)

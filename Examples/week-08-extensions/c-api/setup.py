#!/usr/bin/env python

from setuptools import setup, Extension

setup(
    name='Cadd',
    version='1.0',
    description='simple c extension for an example',
    ext_modules=[Extension('add', sources=['add.c'])],
)

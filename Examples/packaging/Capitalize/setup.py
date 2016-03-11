#!/usr/bin/env python

"""
This is about as simple a setup.py as you can have

It installs the capitalize module and script

"""

from setuptools import setup

import capitalize # to get __version__

setup(
    name='Capitalize',
    version=capitalize.__version__,
    author='Chris Barker',
    author_email='PythonCHB@gmail.com',
    packages=['capitalize',
              'capitalize/test'],
    scripts=['bin/cap_script',],
    license='LICENSE.txt',
    description='Not very useful capitalizing module and script',
    long_description=open('README.txt').read(),
)


#!/usr/bin/env python

"""
simple test for the add C extension
"""

import pytest

import add

def test_basic():
    assert add.add(3,4) == 7

def test_negative():
    assert add.add(-12, 5) == -7

def test_float():
    with pytest.raises(TypeError):
        add.add(3, 4.0)



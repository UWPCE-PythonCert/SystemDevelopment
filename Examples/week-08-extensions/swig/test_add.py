#!/usr/bin/env python

"""
simple test file for SWIG-ified add function
"""

import pytest

from add import add


def test_add1():
    assert add(3, 4) == 7


def test_add_float():
    # only integers!
    with pytest.raises(TypeError):
        assert add(3.1, 4.1) == 7.2


def test_add_string():
    # only integers!
    with pytest.raises(TypeError):
        assert add('2', 4) == 6

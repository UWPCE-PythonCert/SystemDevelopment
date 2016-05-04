#!/usr/bin/env python

"""
tests for an even integer class
"""

from even_int import EvenInt
# from even_int_solution import EvenInt


# And some tests -- try with py.test or nosetests...
def test_subclass():
    assert issubclass(EvenInt, int)


def test_instance():
    i = EvenInt(3)
    assert isinstance(i, int)


def test_isinstance():
    i = EvenInt(2)
    assert isinstance(i, EvenInt)


def test_even():
    assert EvenInt(4) == 4


def test_odd1():
    assert EvenInt(3) == 4


def test_odd2():
    assert EvenInt(2.99) == 2


def test_negative():
    assert EvenInt(-2) == -2


def test_negative_odd():
    assert EvenInt(-1) == 0


def test_negative_odd2():
    assert EvenInt(-1.1) == -2


def test_string_odd():
    assert EvenInt("3") == 4


def test_string_even():
    assert EvenInt("12") == 12


def test_string_float():
    assert EvenInt("4.45") == 4

"""
test file for the divide function
"""

import pytest

from divide import divide


def test_divide():
    assert divide(3, 4) == 0.75


def test_divide_zero():
    # if it acts like python, it should raise an exception
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

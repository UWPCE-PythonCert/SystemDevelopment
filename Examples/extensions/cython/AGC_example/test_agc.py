#!/usr/bin/env python

"""
test code for various AGC modules

designed to be run with py.test or nose

some timing code to cut&paste into iPython:

import numpy as np
import agc_cython
import agc_python
import agc_subroutine
import agc_c_cy

timeit agc_cython.agc(10, np.arange(1000, dtype=np.float32))

timeit agc_python.agc(10, np.arange(1000, dtype=np.float32))

timeit agc_subroutine.agc(10, np.arange(1000, dtype=np.float32))

timeit agc_c_cy.agc(10, np.arange(1000, dtype=np.float32))

"""

import numpy as np

import agc_cython
import agc_python
import agc_c_cy

# The Fortran / f2py version
# import agc_subroutine


def test_cython():
    # just make sure it runs.
    signal = np.arange(20, dtype=np.float32)

    result = agc_cython.agc(4, signal)


def test_c_wrap():
    # just make sure it runs.
    signal = np.arange(20, dtype=np.float32)

    result = agc_c_cy.agc(4, signal)


# def test_subroutine():
#     # the Fortran / f2py version
#     # just make sure it runs.
#     signal = np.arange(20, dtype=np.float32)

#     result = agc_subroutine.agc(4, signal)


def test_cy_py_same():
    signal = np.arange(20, dtype=np.float32)

    cy_result = agc_cython.agc(4, signal)
    py_result = agc_python.agc(4, signal)
    c_cy_result = agc_c_cy.agc(4, signal)
#    sub_result = agc_subroutine.agc(4, signal)

    print "cy:", cy_result
    print "py:", py_result
    print "c_cy", c_cy_result
#    print "subroutine", sub_result

    assert np.array_equal(cy_result, py_result)
    assert np.array_equal(cy_result, c_cy_result)
#    assert np.array_equal(cy_result, sub_result)

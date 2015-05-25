#!/usr/bin/env python

from timer_context import Timer


def run_test(msg):
    print msg
    with Timer():
        result = integrate_f(0.0,10.0,1000000)
    print "result:", result
    print

from integrate import integrate_f
run_test("Pure Python version:")

from cy_integrate1 import integrate_f
run_test("First Cython version:")

from cy_integrate2 import integrate_f
run_test("Second Cython version:")

from cy_integrate3 import integrate_f
run_test("Third Cython version:")

from cy_integrate4 import integrate_f
run_test("Fourth Cython version:")

from cy_integrate5 import integrate_f
run_test("Fifth Cython version:")

from cy_integrate6 import integrate_f
run_test("Sixth Cython version:")

from cy_integrate7 import integrate_f
run_test("Seventh Cython version:")



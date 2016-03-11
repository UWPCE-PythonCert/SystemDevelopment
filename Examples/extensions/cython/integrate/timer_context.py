#!/usr/bin/env python

"""
timer_context

A context manager that does simple code timing

Adapted from:

http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/

NOTE: this is only good for crude timing -- use the timeit module to do it better.
"""

import time

class Timer(object):    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        print "this code took %f seconds"%self.interval

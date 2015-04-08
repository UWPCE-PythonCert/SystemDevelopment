#!/usr/bin/env python

def timer(func):
    import time
    def timer(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        print "\n\n-- function call took: %.4f seconds to run\n\n" % (time.time() - t1)
    return timer

def logger(func):
    def logger(*args, **kwargs):
        print "\n\n-- calling function\n\n"
        func(*args, **kwargs)
        print "\n\n-- function call succeeded\n\n"
    return logger

def exception_handler(func):
    def handle_exceptions(*args, **kwargs):
        try:
            print "handling exceptions.."
            func(*args, **kwargs)
        except Exception as e:
            print "\n\n-- Received exception, logging message: %s\n\n" % str(e)
    return handle_exceptions

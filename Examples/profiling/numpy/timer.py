import time

def timer(func):
    def timer(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print "-- executed %s in %.4f seconds" % (func.func_name, (t2 - t1))
        return result
    return timer


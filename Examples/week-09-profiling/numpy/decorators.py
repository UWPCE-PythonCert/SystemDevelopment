import time

def timer(func):
    def timer(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print "-- executed in %.4f seconds :" % (time.time() - t1)
        return result
    return timer


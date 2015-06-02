import numpy

from timer import timer

@timer
def numpy_test():
    # with open('/usr/share/dict/words') as f:
    arr = numpy.loadtxt('/usr/share/dict/words', dtype='S20')
        # arr = numpy.fromiter( f, dtype='S20' )

    print numpy.char.upper(arr)[0:10]

@timer
def py_test():
    with open('/usr/share/dict/words') as f:
        arr = [x.upper() for x in f]

    print arr[0:10]

py_test()
numpy_test()

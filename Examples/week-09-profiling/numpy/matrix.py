import numpy
import timeit

from decorators import timer

@timer
def offset(matrix, x):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            matrix[i][j] += x

@timer
def numpy_offset(matrix, x):
	"""add x to all values in matix"""
	matrix += x

# create a 2D NxN matrix
python_data_setup = "\
from __main__ import offset;\
N=3000;\
python_data = [[x for x in xrange(N)] for y in xrange(N) ]"

numpy_data_setup = "\
import numpy;\
from __main__ import numpy_offset;\
N=3000;\
numpy_data = numpy.array([[x for x in xrange(N)] for y in xrange(N) ])"

pure_python_statement = "offset(python_data, 10)"
numpy_statement = "numpy_offset(numpy_data, 10)"
print "Pure python: %fs" % timeit.timeit(pure_python_statement, setup=python_data_setup, number=3)
print "Numpy: %fs" % timeit.timeit(numpy_statement, setup=numpy_data_setup, number=3)


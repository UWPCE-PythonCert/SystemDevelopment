#!/usr/bin/env python

"""calculator

    Usage:

    calculator.py 1 + 3

"""

import sys

import calculator_functions as functions

if len(sys.argv) != 4:
    error_message = """

        Invalid arguments.

        Usage:

        calculator.py 1 + 3
        """
    sys.stderr.write(error_message + "\n")
    sys.exit(-1)

x = sys.argv[1]
operator = sys.argv[2]
y = sys.argv[3]

if operator == "+":
    print functions.add(x, y)

elif operator == "-":
    print functions.subtract(x, y)

elif operator == "*":
    print functions.multiply(x, y)

elif operator == "/":
    print functions.divide(x, y)

else:
    print "invalid input"

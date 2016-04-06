#!/usr/bin/env python3

import unittest
import sys
from math import isclose

import calculator_functions as calc
import calculator


class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 3

    def test_add(self):
        self.assertEqual(calc.add(self.x, self.y), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(self.x, self.y), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(self.x, self.y), 6)

    def test_divide(self):
        self.assertTrue(isclose(calc.divide(self.x, self.y), 0.6666666666))


# class TestCalculatorScript(unittest.TestCase):

#     def test_call_not_enough_args(self):
#         "not enough args -- this should give an error return"
#         result = os.system("python calculator.py")
#         print(result)
#         # zero means no error anything else is an error
#         self.assertGreater(result, 0)


class TestCalculatorScript(unittest.TestCase):

    """
    tests the command line script by mangling sys.argv
    """

    def setUp(self):
        """
        here we capture sys.argv so we can put it back when we're done.
        while preserving the old one to put it back
        """
        self.old_argv = sys.argv

    # def test_call_not_enough_args(self):
    #     "not enough args -- this should give an error return"
    #     result = os.system("python calculator.py")
    #     print(result)
    #     # zero means no error anything else is an error
    #     self.assertGreater(result, 0)

    def test_add(self):
        sys.argv = "scriptname 2 + 3".split()
        result = calculator.main()
        self.assertEqual(result, 5)

    def test_subtract(self):
        sys.argv = "scriptname 10 - 2".split()
        result = calculator.main()
        self.assertEqual(result, 8)

    def test_multiply(self):
        sys.argv = "scriptname 10 x 2".split()
        result = calculator.main()
        self.assertEqual(result, 20)

    def test_divide(self):
        sys.argv = "scriptname 10 / 2".split()
        result = calculator.main()
        self.assertEqual(result, 5)

    def test_invalid_operator(self):
        sys.argv = "scriptname 10 $ 2".split()
        result = calculator.main()
        self.assertEqual(result, 'invalid input')

    def test_invalid_nospace(self):
        # Note: there could be a LOT of possible invalid inputs!
        # no space around the "+"
        sys.argv = "scriptname 10+2".split()
        self.assertRaises(ValueError, calculator.main)

    def tearDown(self):
        """ put sys.argv back """
        sys.argv = self.old_argv


if __name__ == "__main__":
    unittest.main()

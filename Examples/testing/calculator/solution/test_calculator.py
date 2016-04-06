import unittest

import calculator_functions as calc
import os


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
        self.assertEqual(calc.divide(self.x, self.y), 2 / 3)


class TestCalculatorScript(unittest.TestCase):

    def test_call_not_enough_args(self):
        "not enough args -- this should give an error return"
        result = os.system("python calculator.py")
        print(result)
        # zero means no error anything else is an error
        self.assertGreater(result, 0)

class TestCalculatorScript(unittest.TestCase):

    def test_call_not_enough_args(self):
        "not enough args -- this should give an error return"
        result = os.system("python calculator.py")
        print(result)
        # zero means no error anything else is an error
        self.assertGreater(result, 0)

    def test_call_not_enough_args(self):
        "not enough args -- this should give an error return"
        result = os.system("python calculator.py")
        print(result)
        # zero means no error anything else is an error
        self.assertGreater(result, 0)



if __name__ == "__main__":
    unittest.main()

import unittest

import calculator_functions as calc

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 3

    def test_add(self):
        self.assertEqual(calc.add(self.x, self.y), 5)

    # def test_add_float(self):
        # self.assertEqual(calc.add(.1,.2), .3)
         

if __name__ == "__main__":
    unittest.main()

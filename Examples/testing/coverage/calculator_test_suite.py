import unittest

from calculator_test import TestCalculatorFunctions

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

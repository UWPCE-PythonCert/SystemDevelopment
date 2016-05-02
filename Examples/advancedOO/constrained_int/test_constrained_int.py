import unittest

from constrained_int import ConstrainedInt


class TestConstrainedInt(unittest.TestCase):

    def test_constrainedint(self):
        x = ConstrainedInt(10)
        self.assertEqual(x, 10)

    def test_constrainedint_mods_correctly(self):
        x = ConstrainedInt(256)
        self.assertEqual(x, 0)

    def test_constrainedint_handles_addition(self):
        x = ConstrainedInt(10)
        x += 246
        self.assertEqual(x, 0)

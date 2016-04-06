import unittest


class TestAlmostEqual(unittest.TestCase):

    def setUp(self):
        pass

    def test_floating_point(self):
        self.assertEqual(3 * .15, .45)

    def test_almost_equal(self):
        self.assertAlmostEqual(3 * .15, .45, places=7)

if __name__ == "__main__":
    unittest.main()

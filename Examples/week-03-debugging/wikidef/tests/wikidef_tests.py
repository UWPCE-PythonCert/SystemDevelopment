import unittest

from api import Wikipedia, ParseError
from definitions import Definitions

class WikiDefTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_article_success(self):
        article = Definitions.article("Robot")        
        self.assertIn("mechanical", article)

    def test_missing_article_failure(self):
        missing_article_title = "!!!!!-NonExistentArticle"
        self.assertRaises(ParseError, Definitions.article, missing_article_title)

    def test_failing_test(self):
        expected = 1
        actual = 0
        self.assertEqual(expected, actual)

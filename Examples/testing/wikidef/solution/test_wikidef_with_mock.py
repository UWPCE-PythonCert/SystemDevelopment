import unittest
import json
from unittest.mock import patch

from api import Wikipedia, ParseError, get_article
from definitions import Definitions

        
class WikiDefTest(unittest.TestCase):

    def setUp(self):
        self.missing_title = "!!!!!-NonExistentArticle"

    def tearDown(self):
        pass

    @patch('api.get_article')
    def test_missing_article_failure(self, mock_get):
        mock_get.return_value = {'error': {'info': "The page you specified doesn't exist"}}
        self.assertRaises(ParseError, Definitions.article, self.missing_title)

    # patch with a decorator
    @patch('definitions.Wikipedia.article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")        
        mock_method.assert_called_once_with("Robot")

    @patch.object(Wikipedia, 'article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")        
        mock_method.assert_called_once_with("Robot")

    # patch with a context manager
    def test_article_success_context_manager_mocked(self):
        with patch.object(Wikipedia, 'article') as mock_method:
            article = Definitions.article("Robot")        
            mock_method.assert_called_once_with("Robot")

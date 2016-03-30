import json
import urllib
# import urllib2


class ParseError(Exception):
    pass


class Wikipedia(object):
    """Wikipedia API interface"""

    api_endpoint = "http://en.wikipedia.org/w/api.php?"

    @classmethod
    def article(cls, title):
        """Return contents of article

        arguments:

        title -- title of article
        """
        query_params = urllib.parse.urlencode({'action': 'parse',
                                               'format': 'json',
                                               'prop': 'text',
                                               'page': 'title'})
        url = cls.api_endpoint + query_params # + 'html'
        response = urllib.request.urlopen(url)
        response_text = response.read().decode('utf-8')
        open('page.json', 'w').write(response_text)
        json_response = json.loads(response_text)
        try:
            contents = json_response['parse']['text']['*']
        except KeyError:
            raise ParseError(json_response)

        return contents

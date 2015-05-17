import json
import urllib
import urllib2

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
        query_params = urllib.urlencode({'action': 'parse', 'format': 'json', 'prop':'text', 'page': title})
        url = cls.api_endpoint + query_params
        response = urllib2.urlopen(url)
        json_response = json.load(response)
        try:
            contents = json_response['parse']['text']['*']
        except KeyError:
            raise ParseError(json_response)

        return contents


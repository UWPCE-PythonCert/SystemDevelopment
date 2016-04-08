import requests


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
        json_response = get_article(title, cls.api_endpoint)
        
        if 'parse' in json_response:
            return json_response['parse']['text']['*']
        else:
            raise ParseError(json_response['error']['info'])


def get_article(title, api_endpoint):
    data = {'action': 'parse', 'format': 'json', 'prop':'text', 'page': title}
    response = requests.get(api_endpoint, params=data)
    return response.json()
    


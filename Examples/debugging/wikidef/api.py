import requests

def article(title):
    """Return contents of article
    
    arguments:
    
    title -- title of article
    """
    api_endpoint = "http://en.wikipedia.org/w/api.php"
    data = {'action': 'parse', 'format': 'json', 'prop':'text', 'page': title}
    response = requests.get(api_endpoint, params=data)
    content_all = response.json()
    contents = content_all['parse']['text']['*']

    return contents


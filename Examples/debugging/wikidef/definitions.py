from api import article

class Definitions(object):

    @classmethod
    def article(cls, title):
        response = article(title)
        return response

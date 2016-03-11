from api import Wikipedia

class Definitions(object):

    @classmethod
    def article(cls, title):
        response = Wikipedia.article(title)
        return response

from api import Wikipedia

class Definitions(object):

    @classmethod
    def article(cls, title):
        return Wikipedia.article(title)

class ConstrainedInt(int):
    """keeps value between 0 and 255"""
    def __new__(cls, value):
        value = value % 256
        self = int.__new__(cls, value)
        return self

    def __add__(self, other):
        return int(self) + int(other)

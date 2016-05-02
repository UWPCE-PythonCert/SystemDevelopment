class Shape:
    def __str__(self):
        return "Shape:{}".format(self.__class__.__name__)


class Rectangle(Shape):
    def __init__(self, width, height):
        # validate inputs:
        assert(width > 0)
        assert(height > 0)

        self.width = width
        self.height = height

    def area(self):
        """returns the area of this Rectangle"""
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

print(Square(10).area())

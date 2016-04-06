"""calculator functions"""

def add(x, y):
    """ Add two numbers

    >>> add(1, 2)
    3
    >>> add(-7, 2)
    -5
    """
    
    return int(x)+int(y)

def subtract(x, y):
    """ Subtract two numbers
    >>> subtract(5, 2)
    4
    >>> subtract(2, 5)
    -3
    """
    return int(x)-int(y)

def multiply(x, y):
    return int(x)*int(y)

def divide(x, y):
    return int(x)/int(y)


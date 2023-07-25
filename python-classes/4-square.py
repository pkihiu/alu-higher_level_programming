#!/usr/bin/python3
'''Defined a class called Square which represents a aquare'''


class Square:
    '''Square class with private size attr'''

    def __init__(self, size=0):
        '''Initializes instances of Square.

           Args:
                size (int): Represents the size of one side of the square.
        '''
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

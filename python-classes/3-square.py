#!/usr/bin/python3
""" python3 -c 'print(__import__("my_module").__doc__)' """


class Square:
    """ python3 -c 'print(__import__("my_module").MyClass.__doc__)' """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @size.getter
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size ** 2

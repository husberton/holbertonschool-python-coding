#!/usr/bin/python3

"""
Docstring for 3-square.py
"""


class Square:

    """
    Docstring for Square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        if not isinstance(self.__size, int):
            raise Exception("size must be an integer")
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()

    def area(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size * self.__size

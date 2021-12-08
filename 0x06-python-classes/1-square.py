#!/usr/bin/python3
# 1-square.py
# Benjamin Taura  <1507@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

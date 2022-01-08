#!/usr/bin/python3
"""Written file"""


def write_file(filename=""):
    """Returns the written file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

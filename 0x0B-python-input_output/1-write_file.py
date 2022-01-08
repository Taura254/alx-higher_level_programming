#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Returns the written file"""
    with open(filename, encoding="utf-8") as f:
        print(f.create(), end="")

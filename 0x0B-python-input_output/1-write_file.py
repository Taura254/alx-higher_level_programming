#!/usr/bin/python3
"""Written file"""


def write_file(filename="",text=""):
    """Returns the written file"""
    with open(filename, 'r') as o:
        linum = 0
        for line in o:
            linum += 1
        return linum

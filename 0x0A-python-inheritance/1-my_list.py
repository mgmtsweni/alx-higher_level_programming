#!/usr/bin/python3
"""function that returns the list"""


class Mylist(list):
    """inharits from list"""

    def print_sorted(self):
        """ prints the list """
        print(sorted(self))

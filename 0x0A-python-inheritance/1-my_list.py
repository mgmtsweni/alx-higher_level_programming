#!/usr/bin/python3
"""function that returns the list"""


class MyList(list):
    """inharits from list"""

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))

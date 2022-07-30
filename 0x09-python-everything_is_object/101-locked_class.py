#!/usr/bin/python3
"""blocked class module"""


class LockedClass:
    """Prevents dynamic new attribute creation"""

    __slots__ = ['first_name']
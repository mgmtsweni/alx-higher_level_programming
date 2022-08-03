#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """inverts == opeartor to != behavior."""
        return self.real != value

    def __ne__(self, value):
        """inverts != operator to == behavior."""
        return self.real == value

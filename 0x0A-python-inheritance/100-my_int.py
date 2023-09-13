
#!/usr/bin/python3
"""Defines
MyINT class that inherits from int.
"""


class MyInt(int):
    def __init__(self, value):
        super().__init__(value)

    def __eq__(self, other):
        # Invert the behavior of ==
        return super().__ne__(other)

    def __ne__(self, other):
        # Invert the behavior of !=
        return super().__eq__(other)

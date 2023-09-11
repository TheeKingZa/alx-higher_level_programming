#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Public instance method to print the list in
        Ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

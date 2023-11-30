#!/usr/bin/python3


def find_peak(list_of_integers):
        """
        Find a peak element in a list of unsorted integers.

        Args:
            - list_of_integers: A list of integers

        Returns:
            - A peak element in the list
            - None if the list is empty
        """

        if not list_of_integers:
            return None

        lo, hi = 0, len(list_of_integers) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if list_of_integers[mid] > list_of_integers[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

        return list_of_integers[lo]

#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak element in a given list using recursive binary search.

    Args:
    - list_of_integers: A list of integers

    Returns:
    - The peak element in the list
    - None if the list is empty or None
    """

    # Check if the input list is empty or None
    if list_of_integers is None or list_of_integers == []:
        return None

    # Initialize variables for binary search
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)

    # Base cases for lists of length 1 or 2
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)

    # Check if the middle element is a peak
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    # Recursively search in the right half if the peak is on the right
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    # Recursively search in the left half if the peak is on the left
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

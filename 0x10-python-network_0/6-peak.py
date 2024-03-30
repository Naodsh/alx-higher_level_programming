#!/usr/bin/python3
"""
Module: 6-peak
Contains function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak element from the list.

    Note:
        A peak is an element which is greater than or equal to its neighbors.

    Complexity:
        The time complexity of this algorithm is O(log(n)).
        This is achieved by employing a binary search approach.
    """
    if not list_of_integers:
        return None
    
    low = 0
    high = len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
            
    return list_of_integers[low]

# Testing the function
if __name__ == "__main__":
    find_peak(list_of_integers)

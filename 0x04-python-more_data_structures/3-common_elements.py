#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Finds the common elements between two sets.

    Args:
        set_1 (set): The first set to compare.
        set_2 (set): The second set to compare.

    Returns:
        set: A new set containing the common elements from both sets.
    """

    common = set()  # Create an empty set to store common elements
    for element in set_1:  # Iterate through elements of set_1
        if element in set_2:  # Check if the element exists in set_2
            common.add(element)  # Add the common element to the result set
    return common

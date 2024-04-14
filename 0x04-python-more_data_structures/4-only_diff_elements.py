#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Finds the elements that are present in only one of the two sets.

    Args:
        set_1 (set): The first set to compare.
        set_2 (set): The second set to compare.

    Returns:
        set: A new set containing the elements that are present in only one set.
    """

    # Use the symmetric difference operation of sets
    return set_1.symmetric_difference(set_2)

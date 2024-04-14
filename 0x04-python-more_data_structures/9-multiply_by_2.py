#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary containing integer values.

    Returns:
        dict: A new dictionary with all values doubled.
    """

    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2  # Double each value and add to new dictionary
    return new_dict

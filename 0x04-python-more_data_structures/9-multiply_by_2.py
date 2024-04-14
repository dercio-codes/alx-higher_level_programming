#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    This function creates a new dictionary with all values in the original dictionary multiplied by 2.

    Parameters:
    a_dictionary (dict): The original dictionary.

    Returns:
    dict: The new dictionary with values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}

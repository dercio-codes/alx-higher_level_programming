#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with keys ordered alphabetically.

    Args:
        a_dictionary (dict): The dictionary to print with sorted keys.
    """

    # Sort keys in alphabetic order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through sorted keys and print key-value pairs
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")

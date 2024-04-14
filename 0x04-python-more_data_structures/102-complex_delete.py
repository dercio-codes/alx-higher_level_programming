#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    This function deletes all keys in a dictionary that have a specific value.

    Parameters:
    a_dictionary (dict): The dictionary to update.
    value: The value to search for in the dictionary.

    Returns:
    dict: The updated dictionary.
    """
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary

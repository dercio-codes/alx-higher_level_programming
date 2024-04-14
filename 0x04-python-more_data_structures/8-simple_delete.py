#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary (if it exists).

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str, optional): The key to delete. Defaults to "".

    Returns:
        None
    """

    if key in a_dictionary:
        del a_dictionary[key]  # Delete the key if it exists
    return a_dictionary

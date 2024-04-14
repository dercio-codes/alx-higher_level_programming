#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary by replacing or adding a key-value pair.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to update or add.
        value: The value to associate with the key.

    Returns:
        None
    """

    a_dictionary[key] = value  # Direct assignment handles both update and addition

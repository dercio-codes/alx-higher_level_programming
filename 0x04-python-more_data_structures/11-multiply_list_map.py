#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number (using map).

    Args:
        my_list (list, optional): The list to multiply elements in. Defaults to [].
        number (int, optional): The number to multiply by. Defaults to 0.

    Returns:
        list: A new list with all values multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))  # One-line solution using map

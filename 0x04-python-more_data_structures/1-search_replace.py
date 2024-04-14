#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of 'search' with 'replace' in a list.

    Args:
        my_list (list): The list to search and replace elements in.
        search: The element to search for.
        replace: The element to replace 'search' with.

    Returns:
        list: A new list with all occurrences of 'search' replaced by 'replace'.
    """

    # Create a new list by replacing all occurrences of 'search' with 'replace'
    new_list = [replace if element == search else element for element in my_list]

    # Return the new list
    return new_list

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list (list, optional): The list to print from. Defaults to [].
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The number of elements actually printed.
    """

    count = 0
    for i in range(len(my_list)):
        try:
            if count == x:
                break
            print(my_list[i], end="")
            count += 1
        except IndexError:
            pass
    print()
    return count

#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    This function calculates the weighted average of all integers in a list of tuples.

    Parameters:
    my_list (list): The list of tuples, where each tuple contains two integers: a score and a weight.

    Returns:
    float: The weighted average of all integers, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_weight = 0
    total_value = 0

    for score, weight in my_list:
        total_weight += weight
        total_value += score * weight

    return total_value / total_weight if total_weight else 0

#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key of the student with the highest score.

    Args:
        a_dictionary (dict): The dictionary containing student scores (integers).

    Returns:
        str: The key (student name) with the highest score.
        None: If the dictionary is empty or no scores are found.
    """

    if not a_dictionary:  # Check if dictionary is empty
        return None

    best_score_key = None
    best_score = float("-inf")  # Initialize with negative infinity

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score_key = key
            best_score = value

    return best_score_key

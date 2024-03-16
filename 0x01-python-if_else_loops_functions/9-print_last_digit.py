#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of the given number.
    Args:
        number (int): The input number.
    Returns:
        None
    """
    # Get the absolute value of the number
    number = abs(number)
    
    # Extract the last digit
    last_digit = number % 10
    
    # Print the last digit
    print(last_digit)

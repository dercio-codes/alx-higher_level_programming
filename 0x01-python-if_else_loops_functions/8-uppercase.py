#!/usr/bin/python3
def uppercase(str):
    """
    Prints the input string in uppercase, followed by a new line.

    Args:
        s (str): The input string.

    Returns:
        None
    """
    for char in str:
        # Convert lowercase letters to uppercase using ord() and chr()
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()  # Print a newline at the end

#!/usr/bin/env python3

import sys

def main():
    # Get the number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:", end=' ')

    # Print each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"\n{i}: {arg}")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for item in reversed(my_list):
        if isinstance(item, int):
            print("{:d}".format(item))
        else:
            print(item)

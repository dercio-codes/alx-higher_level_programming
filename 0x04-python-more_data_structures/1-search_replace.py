#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list by replacing all occurrences of 'search' with 'replace'
    new_list = [replace if element == search else element for element in my_list]
    
    # Return the new list
    return new_list

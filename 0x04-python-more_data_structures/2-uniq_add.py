def uniq_add(my_list=[]):
    # Create a set from the list to remove duplicates
    unique_elements = set(my_list)
    
    # Sum all unique elements in the list
    sum_unique = sum(unique_elements)
    
    # Return the sum
    return sum_unique

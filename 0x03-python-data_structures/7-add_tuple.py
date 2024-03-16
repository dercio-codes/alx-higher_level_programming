#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements
    p_a = tuple_a + (0, 0)
    p_b = tuple_b + (0, 0)
    result = (p_a[0] + p_b[0], p_a[1] + p_b[1])
    return result

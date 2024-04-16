#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  """
  Divides elements of two lists element-wise and returns a new list.

  Args:
      my_list_1 (list): The first list.
      my_list_2 (list): The second list.
      list_length (int): The desired length of the resulting list.

  Returns:
      list: A new list with division results, length `list_length`.
  """
  new_list = []
  for i in range(list_length):
    try:
      if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
        result = my_list_1[i] / my_list_2[i]
      else:
        print("wrong type")
        result = 0
    except ZeroDivisionError:
      print("division by 0")
      result = 0
    except IndexError:
      print("out of range")
      result = 0
    new_list.append(result)
  return new_list

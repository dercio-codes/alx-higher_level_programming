#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
  """
  Prints the first x elements of a list that are integers.

  Args:
      my_list (list, optional): The list to print from. Defaults to [].
      x (int, optional): The number of elements to print. Defaults to 0.

  Returns:
      int: The number of integers actually printed.
  """

  count = 0
  for i in range(len(my_list)):
    try:
      if count == x:
        break
      if isinstance(my_list[i], int):
        print("{:d}".format(my_list[i]), end="")
        count += 1
    except IndexError:
      raise
  print()
  return count

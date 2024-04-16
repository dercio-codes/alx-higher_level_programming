#!/usr/bin/python3
def safe_print_division(a, b):
  """
  Divides two integers and prints the result with error handling.

  Args:
      a (int): The first integer.
      b (int): The second integer.

  Returns:
      float: The result of the division, or None if an error occurs.
  """
  try:
    result = a / b
  except ZeroDivisionError:
    result = None
  finally:
    print("Inside result:", end="")
    if result is not None:
      print(" {:.1f}".format(result))
    else:
      print(" None")
  return result

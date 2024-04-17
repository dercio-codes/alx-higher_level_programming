#!/usr/bin/python3
def append_write(filename="", text=""):
  """
  Appends a string to the end of a text file (UTF-8) and returns the number of characters added.

  Args:
      filename (str, optional): The name of the file to write to. Defaults to "".
      text (str, optional): The text to append to the file. Defaults to "".

  Returns:
      int: The number of characters appended to the file.
  """
  count = 0
  try:
    with open(filename, "a", encoding="utf-8") as file:
      count = len(text)
      file.write(text)
  except UnicodeEncodeError:
    pass
  return count

#!/usr/bin/python3
def write_file(filename="", text=""):
  count = 0
  try:
    with open(filename, "w", encoding="utf-8") as file:
      count = len(text)
      file.write(text)
  except UnicodeEncodeError:
    pass
  return count

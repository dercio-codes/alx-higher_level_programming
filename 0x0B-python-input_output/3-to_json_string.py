#!/usr/bin/python3
import json

def to_json_string(my_obj):
  """
  Returns the JSON representation of an object (string).

  Args:
      my_obj: The object to serialize to JSON.

  Returns:
      str: The JSON representation of the object, or None if serialization fails.
  """
  try:
    return json.dumps(my_obj)
  except (TypeError, OverflowError) as e:
    return None

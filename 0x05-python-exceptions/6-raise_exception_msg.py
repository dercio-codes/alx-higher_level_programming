#!/usr/bin/python3
def raise_exception_msg(message=""):
  """Raises a NameError with a custom message.

  Args:
      message (str, optional): The custom message to include in the exception. Defaults to "".
  """
  # Try to access a non-existent variable
  try:
    non_existent_variable = message  # This will cause a NameError
  except NameError as e:
    # Update the exception message with the provided message
    e.args = (message,)  # Set the exception arguments (message)
    raise e  # Re-raise the modified exception

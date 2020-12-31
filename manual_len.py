# Manual implementation of Python's len() function
# Solve using both an iterative approach and a recursive approach


input_str = "I'm a string, woo! How long am I?"
# print(len(input_str))  Obviously, this works...let's do it manually


# Iterative Approach
def string_length_iterative(input_str):
  length = 0
  for char in input_str:
    length += 1
  return length


# Recursive Approach
# 1. What is the base case?
# 2. How do we make the recursive case smaller?
call_count = 0  # For notes


def string_length_recursive(input_str):
  """
    Each time the fn is called, we increment call_count
    by 1. Notice at the end call_count is 1 more than
    the length of the string.
  """
  global call_count
  call_count += 1
  if input_str == '':
    # We can return anything that will
    # eval to 0 here (e.g. False will work too)
    return 0
  # if input_str has any length at all, recurse!
  return 1 + string_length_recursive(input_str[1:])


print(string_length_iterative(input_str))
print(string_length_recursive(input_str))
print('Recursive call count:', call_count)

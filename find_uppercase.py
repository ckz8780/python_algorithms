# Given an input string, fine the first uppercase letter
# Solve using both an iterative solution and a recursive solution

str_1 = 'secondOnly'
str_2 = 'FirstAndsecond'
str_3 = 'noneatall'


# Iterative Approach
# Iterate each char of the string and check if it's uppercase
def find_uppercase_iterative(input_str):
  for char in input_str:
    if char.isupper():
      return f'Found uppercase char {char}'
  return 'None found'


print(find_uppercase_iterative(str_1))
print(find_uppercase_iterative(str_2))
print(find_uppercase_iterative(str_3))


# Recursive Approach
def find_uppercase_recursive(input_str, i=0):
  if input_str[i].isupper():
    return f'Found uppercae char {input_str[i]}'
  if i == len(input_str) - 1:
    return 'None found'
  return find_uppercase_recursive(input_str, i + 1)


print(find_uppercase_recursive(str_1))
print(find_uppercase_recursive(str_2))
print(find_uppercase_recursive(str_3))

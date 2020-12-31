data = [2, 3, 5, 7, 9, 12, 15, 17, 18, 20, 23, 25, 28, 30, 33, 34, 35, 37]
target = 25


# Linear Search
def linear_search(data, target):
  for i in range(len(data)):
    if data[i] == target:
      return True
  return False


print(linear_search(data, target))


# Iterative Binary Search
# To use binary search, list MUST be SORTED!
def binary_search_iterative(data, target):
  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return False


print(binary_search_iterative(data, target))


# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      return binary_search_recursive(data, target, low, mid - 1)
    else:
      return binary_search_recursive(data, target, mid + 1, high)
  return False


print(binary_search_recursive(data, target, 0, len(data) - 1))

import numpy as np

arr = np.array([41, 42, 43, 44])
filter_arr = []

x = [True, False, True, False]

newarr = arr[x]

print(f"The original array is: {arr}")
print(f"The filtrering array is: {x}")
print(f"the new array created from the filter is: {newarr}")

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(f"The array created from checking is array values are greater than 42 is: {filter_arr}")
print(f" The result of using the above array as a filter for our original numeric array is: {newarr}")
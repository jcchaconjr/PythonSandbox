import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

y = np.where(arr%2 == 1)

print(y)

z = np.searchsorted(arr, 7)

print(f"The index of the searchsorted function for the array index with value 7 is located is {z}.")


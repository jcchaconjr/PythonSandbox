import numpy as np

charArr = np.array(['banana', 'cherry', 'apple'])

print(f"The unsorted array of strings looks like: {charArr}")
print(f"The sorted array of strings now looks like: {np.sort(charArr)}")

boolArr = np.array([True, False, True])

print(f"The unsorted boolean array looks like: {boolArr}")
print(f"The sorted boolean array now looks like: {np.sort(boolArr)}")

arr2D = np.array([[3, 2, 4], [5, 0, 1]])

print(f"The unsorted 2D integer array looks like: {arr2D}")
print(f"The sorted 2D integer array now looks like: {np.sort(arr2D)}")


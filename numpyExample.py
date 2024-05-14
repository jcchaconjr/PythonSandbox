import numpy as np

arr0D = np.array(42)
print(arr0D)

arr1D = np.array([1, 2, 3, 4, 5])
print(arr1D)

arr2D = np.array([[1, 2, 3,], [4, 5, 6]])
print(arr2D)

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3D)

arr4D = np.array([1, 2, 3, 4], ndmin=4)
print(arr4D)

arr5D = np.array([1, 2, 3, 4], ndmin=5)
print(arr5D)
print('\n')

print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)
print(arr4D.ndim)
print(arr5D.ndim)
print('\n')

print("let's print the 3D array:")
print (arr3D[0,1,2])
print('\n')

print("Let's print he 2D array.")
print(arr2D[1,-1])

print("array slicing example:")
addrArr = np.array([[['123', 'Main Street', 'Anytown', 'USA'],['456', 'Elm Avenue', 'Springfield', 'CA']],
                   [['789', 'Oak Drive', 'Lakeside', 'NY'],['321', 'Pine Lane', 'Mountain View', 'TX']]])

print(addrArr[0:1, 0:2, 0:2])
print(f"The type of the above array is: {addrArr.dtype}.")

cnvtArr = np.array([1, 0, 4, -1, 0])
boolarr = cnvtArr.astype(bool)
print(f"the array to convert is: \n {cnvtArr}")
print(f"The bool array is :\n {boolarr}")

print(np.__version__)
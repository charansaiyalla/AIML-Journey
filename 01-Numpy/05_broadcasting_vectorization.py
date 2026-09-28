import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
    # with compatible different shapes
arr = np.array([1, 2, 3])
scalar = 10

print(arr + scalar, "\n")
    # Output : [11 12 13]
    # The scalar value is broadcast to every element


# To perform broadcasting with arrays of different shapes
    # the dimensions must be compatible
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([10, 20, 30])

print(arr1 + arr2, "\n")
    # Output :
    # [[11 22 33]
    #  [14 25 36]]
    # arr2 is broadcast across each row


# Broadcasting with a column array
    # shapes (2, 1) and (2, 3) are compatible
arr1 = np.array([
    [1],
    [2]
])

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr1 + arr2, "\n")
    # Output :
    # [[11 21 31]
    #  [42 52 62]]
    # arr1 is broadcast across each column


# Broadcasting Rules
    # Compare shapes from right to left
    # Dimensions are compatible when:
    # 1. They are equal
    # 2. One of them is 1
    # 3. One dimension is missing


# Compatible shapes
arr1 = np.ones((2, 3))
arr2 = np.ones((3,))

print((arr1 + arr2).shape, "\n")
    # Output : (2, 3)
    # (2, 3) and (3,) are compatible


# Incompatible shapes
arr1 = np.ones((2, 3))
arr2 = np.ones((2,))

# print(arr1 + arr2)
    # Output : ValueError
    # (2, 3) and (2,) are not compatible


# To perform vectorized operations
    # apply operations directly on the entire array
arr = np.array([1, 2, 3, 4, 5])

result = arr * 2 + 10

print(result, "\n")
    # Output : [12 14 16 18 20]
    # Operation is performed on all elements at once


# Vectorization without using a Python loop
    # use NumPy array operations
arr = np.array([1, 2, 3, 4, 5])

result = np.square(arr)

print(result, "\n")
    # Output : [ 1  4  9 16 25]
    # NumPy performs the operation efficiently on the entire array


# Vectorization using mathematical functions
    # use NumPy functions on the complete array
arr = np.array([1, 4, 9, 16])

result = np.sqrt(arr)

print(result, "\n")
    # Output : [1. 2. 3. 4.]
import numpy as np

# To perform operations between NumPy arrays
    # use arithmetic operators
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2, "\n")
    # Output :
    # [5 7 9]
    # [-3 -3 -3]
    # [ 4 10 18]
    # [0.25 0.4  0.5 ]


# To perform operations element-wise
    # use arithmetic operators directly on arrays
arr = np.array([1, 2, 3, 4])

print(arr ** 2)
print(arr + 10, "\n")
    # Output :
    # [ 1  4  9 16]
    # [11 12 13 14]
    # Each element is operated on individually


# To perform scalar operations
    # use an arithmetic operator with a single value
arr = np.array([10, 20, 30, 40])

print(arr * 2)
print(arr / 10, "\n")
    # Output :
    # [20 40 60 80]
    # [1. 2. 3. 4.]
    # The operation is applied to every element


# To perform mathematical functions
    # use NumPy mathematical functions
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))
print(np.square(arr))
print(np.abs([-5, -10, 15]), "\n")
    # Output :
    # [1. 2. 3. 4.]
    # [  1  16  81 256]
    # [ 5 10 15]


# To find the sum of array elements
    # use np.sum()
arr = np.array([10, 20, 30, 40])

print(np.sum(arr), "\n")
    # Output : 100


# To find the minimum and maximum values
    # use np.min() and np.max()
arr = np.array([10, 20, 30, 40])

print(np.min(arr))
print(np.max(arr), "\n")
    # Output :
    # 10
    # 40


# To find the mean, median and standard deviation
    # use np.mean(), np.median() and np.std()
arr = np.array([10, 20, 30, 40, 50])

print(np.mean(arr))
print(np.median(arr))
print(np.std(arr), "\n")
    # Output :
    # 30.0
    # 30.0
    # 14.142135623730951


# To perform aggregation along an axis
    # use axis=0 or axis=1
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1), "\n")
    # Output :
    # [5 7 9]
    # [ 6 15]


# To find the minimum and maximum along an axis
    # use np.min() and np.max() with axis
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.min(arr, axis=0))
print(np.max(arr, axis=1), "\n")
    # Output :
    # [1 2 3]
    # [4 5 6]
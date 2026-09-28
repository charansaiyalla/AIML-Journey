import numpy as np

# To perform element-wise multiplication of matrices
    # use *
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

print(arr1 * arr2, "\n")
    # Output :
    # [[ 5 12]
    #  [21 32]]
    # Each corresponding element is multiplied


# To perform matrix multiplication
    # use @ or np.matmul()
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

print(arr1 @ arr2, "\n")
    # Output :
    # [[19 22]
    #  [43 50]]


# To perform matrix multiplication
    # use np.matmul()
print(np.matmul(arr1, arr2), "\n")
    # Output :
    # [[19 22]
    #  [43 50]]


# To calculate the dot product
    # use np.dot()
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.dot(arr1, arr2), "\n")
    # Output : 32
    # 1×4 + 2×5 + 3×6 = 32


# To transpose a matrix
    # use .T
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T, "\n")
    # Output :
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    # Rows become columns and columns become rows


# To find the inverse of a matrix
    # use np.linalg.inv()    -> linalg = linear algebra
arr = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.inv(arr), "\n")
    # Output :
    # [[-2.   1. ]
    #  [ 1.5 -0.5]]
    # Matrix must be square and non-singular


# To find the determinant of a matrix
    # use np.linalg.det()
arr = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.det(arr), "\n")
    # Output : -2.0


# To perform linear algebra operations
    # use np.linalg
arr = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.det(arr))
print(np.linalg.inv(arr))
print(np.linalg.eig(arr), "\n")
    # np.linalg provides functions for linear algebra
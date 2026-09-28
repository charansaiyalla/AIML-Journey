import numpy as np

# To change the shape of an array
    # use .reshape()
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_arr = arr.reshape(2, 3)

print(reshaped_arr, "\n")
    # Output :
    # [[1 2 3]
    #  [4 5 6]]


# Reshaping Rule
    # Total number of elements must remain the same
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_arr = arr.reshape(3, 2)

print(reshaped_arr, "\n")
    # Output :
    # [[1 2]
    #  [3 4]
    #  [5 6]]
    # 6 elements → 3 × 2 = 6 elements


# To flatten an array into 1D
    # use .flatten()
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat_arr = arr.flatten()

print(flat_arr, "\n")
    # Output : [1 2 3 4 5 6]


# To transpose an array
    # use .T
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transpose_arr = arr.T

print(transpose_arr, "\n")
    # Output :
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    # Rows become columns and columns become rows


# To add a new dimension
    # use np.expand_dims()
arr = np.array([1, 2, 3])

new_arr = np.expand_dims(arr, axis=0)

print(new_arr, "\n")
    # Output :
    # [[1 2 3]]
    # 1D → 2D


# To remove a dimension of size 1
    # use np.squeeze()
arr = np.array([[1, 2, 3]])

new_arr = np.squeeze(arr)

print(new_arr, "\n")
    # Output : [1 2 3]
    # 2D → 1D


# To join arrays along an existing axis
    # use np.concatenate()
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr, "\n")
    # Output : [1 2 3 4 5 6]


# To concatenate 2D arrays row-wise
    # use np.concatenate() with axis=0
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

arr = np.concatenate((arr1, arr2), axis=0)

print(arr, "\n")
    # Output :
    # [[1 2]
    #  [3 4]
    #  [5 6]
    #  [7 8]]


# To concatenate 2D arrays column-wise
    # use np.concatenate() with axis=1
arr = np.concatenate((arr1, arr2), axis=1)

print(arr, "\n")
    # Output :
    # [[1 2 5 6]
    #  [3 4 7 8]]
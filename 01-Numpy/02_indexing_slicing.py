import numpy as np

# To access an element from a NumPy array
    # use indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0], arr[2], "\n")
    # Output : 10 30


# To access elements from the end of an array
    # use negative indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[-1], arr[-2], "\n")
    # Output : 50 40


# To access an element from a 2D array
    # use arr[row, column]
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1], arr[1, 2], "\n")
    # Output : 20 60


# To access elements using negative indexing in a 2D array
    # use negative row or column index
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[-1, -1], arr[-2, -2], "\n")
    # Output : 60 20


# To access a range of elements from an array
    # use slicing [start:stop:step]
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4], "\n")
    # Output : [20 30 40]


# To slice an array from the beginning or to the end
    # use [start:] or [:stop]
arr = np.array([10, 20, 30, 40, 50])

print(arr[:3])
print(arr[2:], "\n")
    # Output :
    # [10 20 30]
    # [30 40 50]


# To slice a 2D array
    # use [rows, columns]
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 1:3], "\n")
    # Output :
    # [[20 30]
    #  [50 60]]


# To select specific rows or columns from a 2D array
    # use slicing with :
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[:, 1], "\n")
    # Output : [20 50 80]


# To select elements based on a condition
    # use boolean indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25], "\n")
    # Output : [30 40 50]


# To select elements using multiple conditions
    # use &, | with conditions
arr = np.array([10, 20, 30, 40, 50])

print(arr[(arr > 20) & (arr < 50)], "\n")
    # Output : [30 40]


# To select specific elements using index positions
    # use fancy indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[[0, 2, 4]], "\n")
    # Output : [10 30 50]


# To select specific rows using fancy indexing
    # use an array of row indices
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[[0, 2]], "\n")
    # Output :
    # [[10 20 30]
    #  [70 80 90]]
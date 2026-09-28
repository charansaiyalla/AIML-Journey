# A NumPy array is a collection of values arranged in one or more dimensions.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr, "\n")

# python list :
numbers = [1, 2, 3, 4, 5]
print(numbers * 2, "\n")
    # Output: [1, 2, 3, 1, 2, 3]

#numpy array :
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 2, "\n")
    # Output: [2 4 6 8 10]
    # This is element-wise numerical computation.
    
# 1-D array
arr = np.array([1, 2, 3])

# 2-D array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr, "\n")

# Multi - Dimensional array
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
print(arr, "\n")

# To find the dimensions 
    # use .ndim 
arr1 = np.array([1, 2, 3]) 
arr2 = np.array([[1, 2], [3, 4]]) 
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 
 
print(arr1.ndim, arr2.ndim, arr3.ndim, "\n") 
    # Output : 1 2 3 
     
# To find the Shape 
    # use .shape 
arr = np.array([[1,2 ,3], [4, 5, 6]]) 

print(arr.shape, "\n") 
    # Output : (2, 3)


# To find the Size 
    # use .size 
arr = np.array([[1,2 ,3], [4, 5, 6]]) 

print(arr.size, "\n") 
    # Output : 6


# To find the Data Type 
    # use .dtype 
arr = np.array([1, 2, 3]) 

print(arr.dtype, "\n") 
    # Output : int64


# To specify the Data Type 
    # use dtype
arr = np.array([1, 2, 3], dtype=float) 

print(arr, arr.dtype, "\n") 
    # Output : [1. 2. 3.] float64

# To create an array of zeros
    # use np.zeros()
arr = np.zeros(5)

print(arr, "\n")
    # Output : [0. 0. 0. 0. 0.]


# To create a 2D array of zeros
    # use np.zeros((rows, columns))
arr = np.zeros((2, 3))

print(arr, "\n")
    # Output :
    # [[0. 0. 0.]
    #  [0. 0. 0.]]


# To create an array of ones
    # use np.ones()
arr = np.ones(5)

print(arr, "\n")
    # Output : [1. 1. 1. 1. 1.]


# To create a 2D array of ones
    # use np.ones((rows, columns))
arr = np.ones((2, 3))

print(arr, "\n")
    # Output :
    # [[1. 1. 1.]
    #  [1. 1. 1.]]


# To create an array with a specific value
    # use np.full()
arr = np.full(5, 7)

print(arr, "\n")
    # Output : [7 7 7 7 7]


# To create a 2D array with a specific value
    # use np.full((rows, columns), value)
arr = np.full((2, 3), 7)

print(arr, "\n")
    # Output :
    # [[7 7 7]
    #  [7 7 7]]


# To create an array with a range of values
    # use np.arange(start, stop, step)
arr = np.arange(1, 10, 2)

print(arr, "\n")
    # Output : [1 3 5 7 9]


# To create evenly spaced values between two numbers
    # use np.linspace(start, stop, number_of_values)
arr = np.linspace(0, 10, 5)

print(arr, "\n")
    # Output : [ 0.   2.5  5.   7.5 10. ]

# To create a copy of an array
    # use .copy()
arr = np.array([1, 2, 3])
copy_arr = arr.copy()

copy_arr[0] = 10

print(arr)
print(copy_arr, "\n")
    # Output :
    # [1 2 3]
    # [10  2  3]
    
# To create a view of an array
    # use .view()
arr = np.array([1, 2, 3])
view_arr = arr.view()

view_arr[0] = 10

print(arr)
print(view_arr, "\n")
    # Output :
    # [10  2  3]
    # [10  2  3]
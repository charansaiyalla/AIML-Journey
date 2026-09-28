import numpy as np


# ============================================================
# EXERCISE 1 — NumPy Array Basics
# ============================================================
#
# Question:
# Create a NumPy array:
# [10, 20, 30, 40, 50]
#
# Print:
# - array
# - number of dimensions
# - shape
# - size
# - data type


# Solution:

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Array :", arr)
print("Dimensions :", arr.ndim)
print("Shape :", arr.shape)
print("Size :", arr.size)
print("Data type :", arr.dtype)

# Output :
# Array : [10 20 30 40 50]
# Dimensions : 1
# Shape : (5,)
# Size : 5
# Data type : int64


# ============================================================
# EXERCISE 2 — Indexing & Slicing
# ============================================================
#
# Question:
# Create:
#
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
#
# Find:
# - 60
# - 80
# - first row
# - last column
# - middle 2 × 2 section


# Solution:

# Create a 2D NumPy array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Find 60
print("60 :", arr[1, 2])

# Find 80
print("80 :", arr[2, 1])

# First row
print("First row :", arr[0, :])

# Last column
print("Last column :", arr[:, -1])

# Middle 2 × 2 section
print("Middle 2 × 2 :\n", arr[0:2, 1:3])

# Output :
# 60 : 60
# 80 : 80
# First row : [10 20 30]
# Last column : [30 60 90]
# Middle 2 × 2 :
# [[20 30]
#  [50 60]]


# ============================================================
# EXERCISE 3 — Boolean Filtering & Aggregation
# ============================================================
#
# Question:
# Create numbers from 1 to 20 and:
# - select even numbers
# - select numbers greater than 10
# - calculate their sum


# Solution:

# Create numbers from 1 to 20
arr = np.arange(1, 21)

# Select even numbers
even_numbers = arr[arr % 2 == 0]
print("Even numbers :", even_numbers)

# Select numbers greater than 10
greater_than_10 = arr[arr > 10]
print("Numbers greater than 10 :", greater_than_10)

# Calculate their sum
print("Sum :", greater_than_10.sum())

# Output :
# Even numbers : [ 2  4  6  8 10 12 14 16 18 20]
# Numbers greater than 10 : [11 12 13 14 15 16 17 18 19 20]
# Sum : 155


# ============================================================
# EXERCISE 4 — Reshape & Flatten
# ============================================================
#
# Question:
# Create an array from 1 to 12.
#
# Reshape it into:
# 3 × 4
#
# Then flatten it again.


# Solution:

# Create an array from 1 to 12
arr = np.arange(1, 13)

# Reshape into 3 × 4
arr_2d = arr.reshape(3, 4)

print("Reshaped array :\n", arr_2d)

# Flatten the array
flattened = arr_2d.flatten()

print("Flattened array :", flattened)

# Output :
# Reshaped array :
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
#
# Flattened array : [ 1  2  3  4  5  6  7  8  9 10 11 12]


# ============================================================
# EXERCISE 5 — Broadcasting
# ============================================================
#
# Question:
# Create:
# [10, 20, 30, 40]
#
# Use broadcasting to:
# - add 5
# - multiply by 2
# - divide by 10


# Solution:

# Create an array
arr = np.array([10, 20, 30, 40])

# Add 5
print("Add 5 :", arr + 5)

# Multiply by 2
print("Multiply by 2 :", arr * 2)

# Divide by 10
print("Divide by 10 :", arr / 10)

# Output :
# Add 5 : [15 25 35 45]
# Multiply by 2 : [20 40 60 80]
# Divide by 10 : [1. 2. 3. 4.]

# Broadcasting applies the scalar operation to every element.


# ============================================================
# EXERCISE 6 — Aggregation & Axis
# ============================================================
#
# Question:
# Create a 3 × 3 matrix and calculate:
# - total
# - row-wise sum
# - column-wise sum
# - mean
# - maximum
# - minimum


# Solution:

# Create a 3 × 3 matrix
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Total
print("Total :", np.sum(arr))

# Row-wise sum
# axis=1 → row-wise
print("Row-wise sum :", np.sum(arr, axis=1))

# Column-wise sum
# axis=0 → column-wise
print("Column-wise sum :", np.sum(arr, axis=0))

# Mean
print("Mean :", np.mean(arr))

# Maximum
print("Maximum :", np.max(arr))

# Minimum
print("Minimum :", np.min(arr))

# Output :
# Total : 450
# Row-wise sum : [ 60 150 240]
# Column-wise sum : [120 150 180]
# Mean : 50.0
# Maximum : 90
# Minimum : 10


# ============================================================
# EXERCISE 7 — Element-wise vs Matrix Multiplication
# ============================================================
#
# Question:
# Create two 2 × 2 matrices.
#
# Calculate:
# 1. Element-wise multiplication
# 2. Matrix multiplication
#
# Understand why the answers are different.


# Solution:

# Create two 2 × 2 matrices
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

# Element-wise multiplication
element_wise = arr1 * arr2
print("Element-wise multiplication :\n", element_wise)

# Matrix multiplication
matrix_multiplication = arr1 @ arr2
print("Matrix multiplication :\n", matrix_multiplication)

# Output :
# Element-wise multiplication :
# [[ 5 12]
#  [21 32]]
#
# Matrix multiplication :
# [[19 22]
#  [43 50]]

# *  → multiplies corresponding elements
# @  → performs mathematical matrix multiplication


# ============================================================
# EXERCISE 8 — AIML-Style Student Marks
# ============================================================
#
# Question:
# Student marks:
#
# 78, 92, 65, 81, 55, 96, 73, 88
#
# Using NumPy:
# - calculate average
# - find highest mark
# - find lowest mark
# - find standard deviation
# - find students above 80
# - find the index of the highest mark


# Solution:

# Create student marks
marks = np.array([78, 92, 65, 81, 55, 96, 73, 88])

# Calculate average
print("Average :", np.mean(marks))

# Find highest mark
print("Highest mark :", np.max(marks))

# Find lowest mark
print("Lowest mark :", np.min(marks))

# Find standard deviation
print("Standard deviation :", np.std(marks))

# Find students above 80
above_80 = marks[marks > 80]
print("Students above 80 :", above_80)

# Find index of highest mark
print("Index of highest mark :", np.argmax(marks))

# Output :
# Average : 78.5
# Highest mark : 96
# Lowest mark : 55
# Standard deviation : 12.964...
# Students above 80 : [92 81 96 88]
# Index of highest mark : 5


# ============================================================
# MINI CHALLENGE — Student Score Analysis
# ============================================================
#
# Question:
# Student scores:
#
# Math      Physics      Chemistry
# 80        75           90
# 65        88           72
# 92        95           89
# 70        60           68
#
# Represent this as a NumPy array.
#
# Then calculate:
# 1. Average of each student
# 2. Average of each subject
# 3. Highest score
# 4. Lowest score
# 5. Students whose average is above 80
# 6. Subject with the highest average
# 7. Total marks of each student


# Solution:

# Create student scores
# columns → Math, Physics, Chemistry
# rows → students
scores = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [92, 95, 89],
    [70, 60, 68]
])

print("Scores :\n", scores)

# Check shape
print("Shape :", scores.shape)

# Average of each student
# axis=1 → row-wise
student_average = np.mean(scores, axis=1)
print("Average of each student :", student_average)

# Average of each subject
# axis=0 → column-wise
subject_average = np.mean(scores, axis=0)
print("Average of each subject :", subject_average)

# Highest score
print("Highest score :", np.max(scores))

# Lowest score
print("Lowest score :", np.min(scores))

# Students whose average is above 80
students_above_80 = scores[student_average > 80]
print("Students above 80 :\n", students_above_80)

# Subject with the highest average
highest_subject_index = np.argmax(subject_average)
print("Subject index with highest average :", highest_subject_index)

# Total marks of each student
student_total = np.sum(scores, axis=1)
print("Total marks of each student :", student_total)

# Output :
# Scores :
# [[80 75 90]
#  [65 88 72]
#  [92 95 89]
#  [70 60 68]]
#
# Shape : (4, 3)
# Average of each student : [81.66666667 75.         92.         66.        ]
# Average of each subject : [76.75 79.5  79.75]
# Highest score : 95
# Lowest score : 60
# Students above 80 :
# [[80 75 90]
#  [92 95 89]]
# Subject index with highest average : 2
# Total marks of each student : [245 225 276 198]

# Subject index:
# 0 → Math
# 1 → Physics
# 2 → Chemistry
#
# Therefore, index 2 represents Chemistry.
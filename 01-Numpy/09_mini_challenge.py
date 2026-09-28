import numpy as np


# ============================================================
# MINI CHALLENGE — Student Score Analysis
# ============================================================
#
# Question:
#
# Create a NumPy array for the following student scores:
#
#              Math    Physics    Chemistry
# Student 1     80       75          90
# Student 2     65       88          72
# Student 3     92       95          89
# Student 4     70       60          68
#
# Then calculate:
#
# 1. Average of each student
# 2. Average of each subject
# 3. Highest score
# 4. Lowest score
# 5. Students whose average is above 80
# 6. Subject with the highest average
# 7. Total marks of each student


# ============================================================
# SOLUTION
# ============================================================

# Create the student scores
# rows → students
# columns → Math, Physics, Chemistry
scores = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [92, 95, 89],
    [70, 60, 68]
])

print("Scores :\n", scores)

# Output :
# Scores :
# [[80 75 90]
#  [65 88 72]
#  [92 95 89]
#  [70 60 68]]


# ============================================================
# 1. Average of each student
# ============================================================

# axis=1 → row-wise
# Each row represents one student
student_average = np.mean(scores, axis=1)

print("Average of each student :", student_average)

# Output :
# Average of each student : [81.66666667 75.         92.         66.        ]


# ============================================================
# 2. Average of each subject
# ============================================================

# axis=0 → column-wise
# Each column represents one subject
subject_average = np.mean(scores, axis=0)

print("Average of each subject :", subject_average)

# Output :
# Average of each subject : [76.75 79.5  79.75]


# ============================================================
# 3. Highest score
# ============================================================

highest_score = np.max(scores)

print("Highest score :", highest_score)

# Output :
# Highest score : 95


# ============================================================
# 4. Lowest score
# ============================================================

lowest_score = np.min(scores)

print("Lowest score :", lowest_score)

# Output :
# Lowest score : 60


# ============================================================
# 5. Students whose average is above 80
# ============================================================

# Create a Boolean condition using student averages
students_above_80 = scores[student_average > 80]

print("Students whose average is above 80 :\n", students_above_80)

# Output :
# Students whose average is above 80 :
# [[80 75 90]
#  [92 95 89]]


# ============================================================
# 6. Subject with the highest average
# ============================================================

# Find the index of the highest subject average
highest_subject_index = np.argmax(subject_average)

print("Index of subject with highest average :", highest_subject_index)

# Subject index:
# 0 → Math
# 1 → Physics
# 2 → Chemistry

# Output :
# Index of subject with highest average : 2

# Therefore:
# Chemistry has the highest average.


# ============================================================
# 7. Total marks of each student
# ============================================================

# axis=1 → row-wise
# Add all subject marks for each student
student_total = np.sum(scores, axis=1)

print("Total marks of each student :", student_total)

# Output :
# Total marks of each student : [245 225 276 198]


# ============================================================
# FINAL OUTPUT SUMMARY
# ============================================================
#
# Student averages :
# [81.66666667 75.         92.         66.        ]
#
# Subject averages :
# [76.75 79.5  79.75]
#
# Highest score : 95
#
# Lowest score : 60
#
# Students above 80 average :
# [[80 75 90]
#  [92 95 89]]
#
# Subject with highest average :
# Chemistry
#
# Total marks of each student :
# [245 225 276 198]
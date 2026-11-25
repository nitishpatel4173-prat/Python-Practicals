# Practical 38: Merge two DataFrames on a common key (StudentID)

import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Aarav", "Diya", "Kabir", "Meera"],
})

marks = pd.DataFrame({
    "StudentID": [101, 102, 103, 105],
    "Python": [88, 76, 91, 67],
})

print("students:")
print(students)
print("\nmarks:")
print(marks)

# inner: only keys present in both tables
print("\nInner merge:")
print(pd.merge(students, marks, on="StudentID", how="inner"))

# left: all rows of students; missing marks become NaN
print("\nLeft merge:")
print(pd.merge(students, marks, on="StudentID", how="left"))

# outer: all rows of both tables
print("\nOuter merge:")
print(pd.merge(students, marks, on="StudentID", how="outer"))

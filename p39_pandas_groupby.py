# Practical 39: groupby() with aggregate functions

import pandas as pd

employees = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales", "IT"],
    "Employee": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sara", "Isha"],
    "Salary": [50000, 40000, 65000, 45000, 42000, 52000, 58000],
})

print("Data:")
print(employees)

print("\nTotal salary per department:")
print(employees.groupby("Department")["Salary"].sum())

print("\nAverage salary per department:")
print(employees.groupby("Department")["Salary"].mean())

print("\nNumber of employees per department:")
print(employees.groupby("Department")["Employee"].count())

print("\nSeveral aggregates together:")
summary = employees.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"])
print(summary)

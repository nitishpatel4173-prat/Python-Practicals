# Practical 37: Create a pandas DataFrame and filter data
# Install once (macOS Terminal):  pip3 install pandas

import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sara"],
    "City": ["Vadodara", "Surat", "Vadodara", "Ahmedabad", "Surat", "Vadodara"],
    "Marks": [85, 72, 91, 66, 78, 59],
}
df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nMarks greater than 75:")
print(df[df["Marks"] > 75])

print("\nStudents from Vadodara:")
print(df[df["City"] == "Vadodara"])

print("\nVadodara AND Marks >= 80:")
print(df[(df["City"] == "Vadodara") & (df["Marks"] >= 80)])

print("\nName and City of students from Surat or Ahmedabad:")
print(df[df["City"].isin(["Surat", "Ahmedabad"])][["Name", "City"]])

print("\nUsing query() - Marks less than 70:")
print(df.query("Marks < 70"))

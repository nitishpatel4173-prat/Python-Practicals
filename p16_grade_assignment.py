# Practical 16: Grade assignment based on score (out of 100)

score = float(input("Enter the student's score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score! Enter a value between 0 and 100.")
elif score >= 90:
    print("Grade: A+  (Outstanding)")
elif score >= 80:
    print("Grade: A   (Excellent)")
elif score >= 70:
    print("Grade: B   (Very Good)")
elif score >= 60:
    print("Grade: C   (Good)")
elif score >= 50:
    print("Grade: D   (Satisfactory)")
elif score >= 40:
    print("Grade: E   (Pass)")
else:
    print("Grade: F   (Fail)")

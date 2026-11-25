# Practical 12: Voting eligibility check

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You are not eligible to vote. Please wait {18 - age} more year(s).")

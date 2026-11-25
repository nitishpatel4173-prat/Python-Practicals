# Practical 13: Age group classification using nested if-elif-else

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age! Age cannot be negative.")
else:
    # nested block: runs only when the age is valid
    if age <= 12:
        print("Age group: Child")
    elif age <= 19:
        print("Age group: Teenager")
    elif age <= 59:
        print("Age group: Adult")
    else:
        print("Age group: Senior Citizen")

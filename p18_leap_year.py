# Practical 18: Leap year check
# Rule: divisible by 4 AND not divisible by 100, OR divisible by 400

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

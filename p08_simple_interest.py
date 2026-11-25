# Practical 8: Simple Interest  SI = (P * R * T) / 100

principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter rate of interest per year (R %): "))
years = float(input("Enter time in years (T): "))

simple_interest = (principal * rate * years) / 100
total_amount = principal + simple_interest

print(f"Simple Interest = {simple_interest:.2f}")
print(f"Total Amount    = {total_amount:.2f}")

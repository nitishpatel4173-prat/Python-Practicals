# Practical 46: Exception handling - division by zero

try:
    numerator = float(input("Enter numerator  : "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not possible.")
except ValueError:
    print("Error: Please enter valid numbers only.")
else:
    print(f"Result = {result}")          # runs only when no exception occurred
finally:
    print("Program finished.")           # always runs

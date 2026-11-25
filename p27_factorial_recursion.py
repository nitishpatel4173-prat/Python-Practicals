# Practical 27: Factorial using recursion


def factorial(n):
    """Return n! (n factorial) using recursion."""
    if n == 0 or n == 1:               # base case: stops the recursion
        return 1
    return n * factorial(n - 1)        # recursive case


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} = {factorial(number)}")

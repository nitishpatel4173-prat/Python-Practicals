# Practical 31: Square root using the math module

import math

number = float(input("Enter a number: "))

if number < 0:
    print("Square root of a negative number is not a real number.")
else:
    root = math.sqrt(number)
    print(f"Square root of {number:g} = {root:.4f}")
    print("Floor of the root :", math.floor(root))
    print("Ceil of the root  :", math.ceil(root))

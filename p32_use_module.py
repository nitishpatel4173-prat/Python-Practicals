# Practical 32 (main program): use the user-defined module multiply_module

import multiply_module                     # style 1: import the whole module
from multiply_module import multiply       # style 2: import one function

x = float(input("Enter first number : "))
y = float(input("Enter second number: "))

print(f"Using module name : {x} x {y} = {multiply_module.multiply(x, y)}")
print(f"Using direct name : {x} x {y} = {multiply(x, y)}")

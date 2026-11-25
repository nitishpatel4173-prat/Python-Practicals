# Practical 1: Swap two numbers without a third variable and without arithmetic operators

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, ", b =", b)

# Tuple packing / unpacking: the right side (b, a) is evaluated first,
# then its values are assigned to a and b in order.
a, b = b, a

print("After swapping : a =", a, ", b =", b)

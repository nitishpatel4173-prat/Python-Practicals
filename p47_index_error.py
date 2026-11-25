# Practical 47: Catch and handle IndexError

fruits = ["apple", "banana", "cherry", "mango"]
print("List:", fruits, "(valid indexes 0 to 3, or -1 to -4)")

try:
    index = int(input("Enter an index to access: "))
    print("Element at that position:", fruits[index])
except IndexError:
    print(f"IndexError: index {index} is out of range for a list of {len(fruits)} items.")
except ValueError:
    print("ValueError: please enter a whole number.")

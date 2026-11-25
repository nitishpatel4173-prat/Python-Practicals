# Practical 23: Print only the unique values of a list (remove duplicates)

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
print("Original list :", numbers)

# Method 1: loop and keep the first occurrence (keeps the original order)
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Unique (loop)           :", unique_numbers)

# Method 2: dict.fromkeys() removes duplicates and keeps the order
print("Unique (dict.fromkeys)  :", list(dict.fromkeys(numbers)))

# Method 3: set() removes duplicates but does not keep the order
print("Unique (set, sorted)    :", sorted(set(numbers)))

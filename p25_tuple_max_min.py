# Practical 25: Maximum and minimum value from a tuple

numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    print("Tuple   :", numbers)
    print("Maximum :", max(numbers))
    print("Minimum :", min(numbers))

    # Same result without built-in functions
    largest = smallest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    print("Using loop -> Maximum:", largest, "| Minimum:", smallest)

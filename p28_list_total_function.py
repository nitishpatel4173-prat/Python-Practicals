# Practical 28: Function to compute the total of a list


def list_total(numbers):
    """Return the sum of all elements in the list."""
    total = 0
    for value in numbers:
        total += value
    return total


data = list(map(float, input("Enter numbers separated by spaces: ").split()))

print("List  :", data)
print("Total :", list_total(data))
print("Check with built-in sum():", sum(data))

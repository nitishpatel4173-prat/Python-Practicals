# Practical 33: Random number between 1 and 100

import random

number = random.randint(1, 100)       # both 1 and 100 are possible
print("Random number between 1 and 100:", number)

# Generate five more random numbers
numbers = [random.randint(1, 100) for _ in range(5)]
print("Five more random numbers       :", numbers)

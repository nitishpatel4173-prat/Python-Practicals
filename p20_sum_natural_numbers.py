# Practical 20: Sum of first n natural numbers using a while loop

n = int(input("Enter a positive integer n: "))

if n < 1:
    print("Please enter a number greater than 0.")
else:
    total = 0
    counter = 1
    while counter <= n:        # repeat until the counter passes n
        total += counter       # add the current number
        counter += 1           # move to the next number

    print(f"Sum of first {n} natural numbers = {total}")
    print(f"Check using formula n(n+1)/2      = {n * (n + 1) // 2}")

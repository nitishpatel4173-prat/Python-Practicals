# Practical 19: Multiplication tables from 1 to 5 using nested loops

for table in range(1, 6):                 # outer loop: tables 1 to 5
    print(f"--- Multiplication table of {table} ---")
    for multiplier in range(1, 11):       # inner loop: 1 to 10
        print(f"{table} x {multiplier:2} = {table * multiplier:3}")
    print()                               # blank line after each table

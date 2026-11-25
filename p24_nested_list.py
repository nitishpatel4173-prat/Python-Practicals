# Practical 24: Access all elements of a nested list using loops

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("--- Row by row ---")
for row in matrix:
    print(row)

print("\n--- Every element using nested loops ---")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("\n--- Using index positions ---")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

print("\n--- Nested list with rows of different length ---")
students = [["Aarav", 85, 90], ["Diya", 78], ["Kabir", 92, 88, 95]]
for record in students:
    for item in record:
        print(item, end=" | ")
    print()

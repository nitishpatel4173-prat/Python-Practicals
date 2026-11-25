# Practical 36: Solve a system of linear equations with numpy.linalg.solve()
#    2x +  y -  z =   8
#   -3x -  y + 2z = -11
#   -2x +  y + 2z =  -3

import numpy as np

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])          # coefficient matrix
b = np.array([8, -11, -3])          # constants on the right-hand side

solution = np.linalg.solve(A, b)
x, y, z = solution

print("Coefficient matrix A:\n", A)
print("Constants b         :", b)
print(f"\nSolution: x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

# Verification: A @ solution must be equal to b
print("Verification (A @ solution == b):", np.allclose(A @ solution, b))

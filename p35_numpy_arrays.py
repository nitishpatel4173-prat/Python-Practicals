# Practical 35: Access and manipulate array elements using NumPy
# Install once (macOS Terminal):  pip3 install numpy

import numpy as np

# ---------- 1-D array ----------
arr = np.array([10, 20, 30, 40, 50, 60])
print("Array           :", arr)
print("Shape / Size    :", arr.shape, "/", arr.size)
print("First, last     :", arr[0], arr[-1])
print("arr[1:4]        :", arr[1:4])

arr[0] = 15                     # change one element
arr[-1] = 65
print("After changing  :", arr)

print("arr * 2         :", arr * 2)
print("arr > 30        :", arr > 30)
print("arr[arr > 30]   :", arr[arr > 30])     # boolean indexing

# ---------- 2-D array ----------
matrix = np.arange(1, 13).reshape(3, 4)
print("\nMatrix (3 x 4):\n", matrix)
print("matrix[1, 2]    :", matrix[1, 2])       # row 1, column 2
print("matrix[0, :]    :", matrix[0, :])       # first row
print("matrix[:, 1]    :", matrix[:, 1])       # second column
print("matrix[1:, 2:]  :\n", matrix[1:, 2:])   # sub-matrix

# ---------- Useful NumPy functions ----------
print("\nSum / Mean      :", arr.sum(), "/", arr.mean())
print("Max / Min       :", arr.max(), "/", arr.min())
print("Index of max    :", arr.argmax())
print("Sorted desc     :", np.sort(arr)[::-1])
print("Column sums     :", matrix.sum(axis=0))
print("Row sums        :", matrix.sum(axis=1))

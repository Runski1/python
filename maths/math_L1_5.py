import numpy as np
import numpy.linalg
import numpy.linalg as la
from sympy import symbols, solve

mat_A = np.array([[-1, 2], [3, -1]])
mat_B = np.array([[0, 1, 3], [2, -3, 5]])
mat_C = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
mat_D = np.array([1, -3, 1])
mat_E = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
mat_F = np.array([3, -5, 7])
mat_G = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
mat_H = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
matrices = [mat_A, mat_B, mat_C, mat_D, mat_E, mat_F, mat_G, mat_H]
print("a) ")
print(np.dot(mat_A, mat_B))
print("b) ")
print(np.dot(mat_C, mat_D))
print("c) ")
print(np.dot(mat_E, mat_F))
print("d) ")
print(np.dot(mat_G, mat_H))
print("2. Edeltävien matriisien transpoosit ja determinantit")
for matrix in matrices:
    try:
        print(np.linalg.det(matrix), np.transpose(matrix))
    except numpy.linalg.LinAlgError:
        print("Matrix not a square matrix")

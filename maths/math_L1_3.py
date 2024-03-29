import numpy as np
import numpy.linalg as la
from sympy import symbols, solve

matrix_A = np.array([[-1, 2], [3, -5]])
matrix_B = np.array([[2, 0], [-1, 4]])
print("2A + 3B = ")
print(2 * matrix_A + 3 * matrix_B)
print("A - B = ")
print(matrix_A - matrix_B)

matrix_aA = np.array([[5, 3], [2, 1]])
matrix_aB = np.array([[9], [4]])
matrix_bA = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
matrix_bB = np.array([[6], [2], [9]])
matrix_cA = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
matrix_cB = np.array([[-1], [5], [2]])

matrix_aX = la.inv(matrix_aA).dot(matrix_aB)
print("matrix_aX = ")
print(matrix_aX)
matrix_bX = la.inv(matrix_bA).dot(matrix_bB)
print("matrix_bX = ")
print(matrix_bX)
try:
    matrix_cX = la.inv(matrix_cA).dot(matrix_cB)
    print("matrix_cX = ")
    print(matrix_cX)
except la.LinAlgError:
    print("matrix_cA is not invertible")
    # If determinant of matrix_cA is 0, matrix is singular and thus not invertible
    print("det(matrix_aA) = ")
    print(la.det(matrix_cA))
    x, y, z = symbols('x y z')
    print("solved symbolically using sympy")
    print(solve([x + y + 3*z + 1, 3*x + y + z - 5, 2 * x + y + 2 * z - 2], [x, y, z]))


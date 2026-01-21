import numpy as np

r1 = int(input("Enter number of rows of Matrix A: "))
c1 = int(input("Enter number of columns of Matrix A: "))
r2 = int(input("Enter number of rows of Matrix B: "))
c2 = int(input("Enter number of columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    print("Enter elements of Matrix A:")
    A = np.array([[int(input()) for j in range(c1)] for i in range(r1)])
    print("Enter elements of Matrix B:")
    B = np.array([[int(input()) for j in range(c2)] for i in range(r2)])
    result = np.dot(A, B)
    print("Resultant Matrix:")
    print(result)

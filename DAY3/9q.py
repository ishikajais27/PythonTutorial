r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter first matrix:")
m1 = [[int(input()) for j in range(c)] for i in range(r)]

print("Enter second matrix:")
m2 = [[int(input()) for j in range(c)] for i in range(r)]

add = [[m1[i][j] + m2[i][j] for j in range(c)] for i in range(r)]
sub = [[m1[i][j] - m2[i][j] for j in range(c)] for i in range(r)]

print("Matrix Addition:")
for row in add:
    print(row)

print("Matrix Subtraction:")
for row in sub:
    print(row)

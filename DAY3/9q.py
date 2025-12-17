matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

add = [[0, 0], [0, 0]]
sub = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        add[i][j] = matrix1[i][j] + matrix2[i][j]
        sub[i][j] = matrix1[i][j] - matrix2[i][j]

print("Matrix Addition:", add)
print("Matrix Subtraction:", sub)

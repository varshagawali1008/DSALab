matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Row-wise sum
for i in range(3):
    row_sum = 0
    for j in range(3):
        row_sum += matrix[i][j]
    print("Sum of Row", i + 1, "=", row_sum)

# Column-wise sum
for j in range(3):
    col_sum = 0
    for i in range(3):
        col_sum += matrix[i][j]
    print("Sum of Column", j + 1, "=", col_sum)

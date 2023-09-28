def matrix_rotate_right(matrix):
    if not matrix:
        return []

    nRows, nCols = len(matrix), len(matrix[0])
    rotated = []

    for j in range(nCols):
        rotatedRow = []
        for i in range(nRows - 1, -1, -1):
            rotatedRow.append(matrix[i][j])
        rotated.append(rotatedRow)

    return rotated

#I added this hehe
def matrix_rotate_left(matrix):
    if not matrix:
        return []

    nRows, nCols = len(matrix), len(matrix[0])
    rotated = []

    for j in range(nCols - 1, -1, -1):
        rotatedRow = []
        for i in range(nRows):
            rotatedRow.append(matrix[i][j])
        rotated.append(rotatedRow)

    return rotated

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = matrix_rotate_right(matrix)
for row in rotated:
    print(row)

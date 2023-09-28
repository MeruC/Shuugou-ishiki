def flatten(matrix):
    flat = [elem for row in matrix for elem in row]
    return flat

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = flatten(matrix)
print(flat)
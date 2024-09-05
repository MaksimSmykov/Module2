def get_matrix (n, m, value):
    matrix = []
    for n1 in range(n):
        matrix.append([])
        for m1 in range(m):
            matrix[n1].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
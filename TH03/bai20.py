matrix = [
    [2, 4, 6],
    [6, 1, 2],
    [7, 9, 7]
]
tong_chinh = 0
tong_phu = 0
for i in range(len(matrix)):
    tong_chinh += matrix[i][i]
    tong_phu += matrix[i][len(matrix) - 1 - i]
print("Tổng đường chéo chính:", tong_chinh)
print("Tổng đường chéo phụ:", tong_phu)
result = tuple(tuple(row) for row in matrix)
print("Tuple:", result)

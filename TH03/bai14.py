data = [(1,2), (6,7), (9,12)]
tong_x = 0
tong_y = 0
for x, y in data:
    tong_x += x
    tong_y += y
tb_x = tong_x / len(data)
tb_y = tong_y / len(data)
print("Trung bình x:", tb_x)
print("Trung bình y:", tb_y)

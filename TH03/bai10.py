n = list(map(int, input("Nhập ds: ").split()))
max_count = 0
max_value = None
for x in n:
    so_lan = n.count(x)
    if so_lan > max_count:
        max_count = so_lan
        max_value = x
print("Phần tử xuất hiện nhiều nhất:", max_value)
print("Số lần xuất hiện:", max_count)

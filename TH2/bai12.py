n=list(map(int,input("Nhập ds:").split()))
max_count = 0
max_n = n[0]
for x in n:
    count = n.count(x)
    if count > max_count:
        max_count = count
        max_n = x
print("Phần tử xuất hiện nhiều nhất: ", max_n)
print("Số lần xuất hiện: ", max_count)

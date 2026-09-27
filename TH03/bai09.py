n = list(map(int,input("Nhập 1 ds: ").split()))
m = []
for i in n:
    if i not in m:
        m.append(i)
print("Ds sau khi loại bỏ trùng: ", m)

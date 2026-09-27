chuoi = input("Nhập chuỗi: ")
dem = {}
for i in chuoi:
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
print(dem)

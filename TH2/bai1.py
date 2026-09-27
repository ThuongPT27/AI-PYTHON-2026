chuoi=input("Nhập 1 chuỗi: ")
print("Độ dài chuỗi: ",len(chuoi))
for i in set(chuoi):
    print(i,":",chuoi.count(i))

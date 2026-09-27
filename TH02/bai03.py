chuoi=input("Nhập 1 chuỗi: ")
nguyen_am=["u","e","o","a","i"]
so_nguyen_am=0
so_phu_am=0
for i in chuoi:
    if i in nguyen_am:
        so_nguyen_am +=1
    else:
        so_phu_am +=1
print("Số nguyên âm là: ",so_nguyen_am )
print("Số phụ âm là: ", so_phu_am)

import random
so_bi_mat=random.randint(1,10)
so_doan=int(input("Nhập số đoán: "))
while so_doan != so_bi_mat:
    if so_doan < so_bi_mat:
        print("Lớn hơn")
    else:
        print("Nhỏ hơn")
    so_doan=int(input("Mời bạn đoán lại:"))
print("Chúc mừng bạn đã đoán đúng!")

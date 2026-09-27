#Bài 1
name = "Thương"
age = 18
school = "PTIT"
print("Xin chào, tôi là", name ,",năm nay",age,"tuổi, đang học tại",school,".")

#Bài 2:
chieu_dai=float(input("Nhập chiều dài: "))
chieu_rong=float(input("Nhập chiều rộng: "))
chu_vi=(chieu_dai+chieu_rong)*2
dien_tich=chieu_dai*chieu_rong
print("Chu vi hcn là:",chu_vi)
print("Diện tích hcn là:", dien_tich)

#Bài 3:
C=int(input("Nhiệt độ (độ C):"))
F=C*9/5+32
print("Nhiệt độ (độ F):",F)

#Bài 4:
T,A,V=list(map(float,input("Nhập điểm Toán, Văn, Anh: ").split()))
tb=(T+V+A)/3
print("Điểm trung bình:",round(tb,2))

#Bài 5:
ten=str(input("Nhập tên của bạn: "))
tuoi=int(input("Nhập tuổi của bạn: "))
print("Tôi tên là",ten,", tôi",tuoi,"tuổi.")
print("Sang năm tôi sẽ",tuoi+1,"tuổi.")

#Bài 6:
n=int(input("Nhập 1 số nguyên: "))
if n%2==0:
    print("Số chẵn")
else:
    print("Số lẻ")

#Bài 7:
a,b=list(map(float,input("Nhập a,b: ").split()))
if a>b:
    print(a)
else:
    print(b)

#Bài 8:
diem_tb=float(input("Nhập điểm trung bình: "))
if 8 <= diem_tb <= 10:
    print ("Giỏi")
elif 6.5 <= diem_tb <= 7.9:
    print("Khá")
elif 5 <= diem_tb <= 6.4:
    print ("Trung bình")
else:
    print("Yếu")

#Bài 9: 
so_kWh=int(input("Nhập số kWh tiêu thụ: "))
tong_tien=0
if 0 <= so_kWh <= 50:
    tong_tien= so_kWh* 1800
elif 51 <= so_kWh <= 100:
    tong_tien=50*1800+(so_kWh-50)*2000
else:
    tong_tien=50*1800+50*2000+(so_kWh-100)*2500
print(tong_tien)

#Bài 10:
n=int(input("Nhập 1 năm: "))
if  n%400==0 or (n%4==0 and n%100!=0):
    print("Năm nhuận")
else:
    print("Năm không nhuận")

#Bài 11:
n=int(input("Nhập 1 số (1-9): "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#Bài 12:
n=int(input("Nhập n: "))
tong=0
for i in range(n+1):
    tong=tong+i
print(tong)

#Bài 13:
n=int(input("Nhập số nguyên:"))
so_chan=0
for i in range (n+1):
    if i%2==0:
        so_chan+=1
print(so_chan)

#Bài 14:
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

#Bài 15:
n=int(input("Nhập số hàng: "))
for i in range (1,n+1):
    print (i*"*")

n=list(map(int,input("Nhập ds:").split()))
tong=0
for i in n:
    if i%2==0:
        tong+=i
print("Tổng số chẵn: ",tong)

n=list(map(int,input("Nhập ds số nguyên: ").split()))
m=[]
for i in n:
    if i>10 and i%2==0:
        m.append(i)
print("Ds mới: ", m)
        

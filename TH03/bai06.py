n=list(map(int,input("Nhập 1 ds: ").split()))
m=[]
for i in range (len(n)-1,-1,-1):
    m.append(n[i])
print("Ds đảo ngược: ",m)

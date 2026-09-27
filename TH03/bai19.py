n = list(map(int, input("Nhập ds: ").split()))
N = int(input("Nhập N: "))
min_khoang_cach = float("inf")
cap = ()
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        tong = n[i] + n[j]
        khoang_cach = abs(tong - N)
        if khoang_cach < min_khoang_cach:
            min_khoang_cach = khoang_cach
            cap = (n[i], n[j])
print("Cặp gần nhất:", cap)
print("Tổng:", cap[0] + cap[1])

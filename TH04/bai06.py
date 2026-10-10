def ptu_trung(ds):
    return list(dict.fromkeys(ds))
a=list(map(int,input().split()))
print(ptu_trung(a))

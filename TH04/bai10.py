def loc(ds):
    return [x for x in ds if x % 2 == 0 and x > 10]

a=list(map(int,input().split()))
print(loc(a))

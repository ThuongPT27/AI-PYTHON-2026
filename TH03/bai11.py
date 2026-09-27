d1 = {"A": 5, "B": 9}
d2 = {"A": 2, "C": 2007}
for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

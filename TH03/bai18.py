data = [
    ("A01", 7),
    ("B01", 9),
    ("A01", 6)
]
tong = {}
for sku, quantity in data:
    if sku in tong:
        tong[sku] += quantity
    else:
        tong[sku] = quantity
result = list(tong.items())
print(result)

diem = {
    "Anh": 7,
    "Bình": 9,
    "Nam": 8,
    "Mai": 7.5,
    "Thanh": 8.25
}
ket_qua = sorted(diem.items(), key=lambda x: x[1], reverse=True)
for ten, diem_so in ket_qua:
    print(ten, diem_so)

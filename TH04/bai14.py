def dtb(ds):
    if not ds:
        return 0
    return sum(ds) / len(ds)

def ploai(diem_tb):
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def ptich(dssv):
    return {ten: ploai(dtb(ds)) for ten, ds in dssv.items()}

def doc(ten_file):
    ket_qua = {}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for dong in f:
                dong = dong.strip()
                if not dong:
                  continue
                ten, diem = dong.split(maxsplit=1)
                if ten not in ket_qua:
                    ket_qua[ten] = []
                ket_qua[ten].append(int(diem))
    except FileNotFoundError:
        print("Không tìm thấy file!")
    return ket_qua

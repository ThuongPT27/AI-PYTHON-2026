def doc(ten_file):
    lst_tuple = []
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for dong in f:
                dong = dong.strip()
                if dong:
                    ten, diem = dong.split(maxsplit=1)
                    lst_tuple.append((ten, int(diem)))
    except FileNotFoundError:
        pass
    return lst_tuple
  
def tong_hop(lst_tuple):
    dict_tam = {}
    for ten, diem in lst_tuple:
        if ten not in dict_tam:
            dict_tam[ten] = []
        dict_tam[ten].append(diem)
    dict_tb = {}
    for ten, lst_diem in dict_tam.items():
        dict_tb[ten] = sum(lst_diem) / len(lst_diem)
    return dict_tb

def ghi_ket_qua(dict_tb, ten_file_ghi):
    with open(ten_file_ghi, 'w', encoding='utf-8') as f:
        for ten, diem_tb in dict_tb.items():
            f.write(f"{ten}: {diem_tb:.1f}\n")

def xu_ly(file_nguon="scores.txt", file_dich="result.txt"):
    du_lieu_tho = doc(file_nguon)
    dict_trung_binh = tong_hop(du_lieu_tho)
    ghi_ket_qua(dict_trung_binh, file_dich)

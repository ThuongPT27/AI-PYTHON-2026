def gop(ds1,ds2):
    ket_qua = ds1.copy()
    for key, value in ds2.items():
        if key in ket_qua:
            ket_qua[key] += value
        else:
            ket_qua[key] = value  
    return ket_qua

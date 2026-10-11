def nhom_ptu(ds):
    ket_qua = {}
    for vtri,gtri in enumerate(ds):
        if gtri not in ket_qua:
            ket_qua[gtri] = []
        ket_qua[gtri].append(vtri)
    return ket_qua

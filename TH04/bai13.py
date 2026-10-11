def gop(ds):
    dict_tam = {}
    for ma_id, gtri in ds:
        if ma_id not in dict_tam:
            dict_tam[ma_id] = []
        dict_tam[ma_id].append(gtri)
    return [(ma_id, tuple(gtri)) for ma_id, gtri in dict_tam.items()]

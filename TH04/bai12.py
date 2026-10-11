def cht(ds):
    dsch = []
    for ten in ds:
        ten_chuan = ten.strip().title()
        if ten_chuan not in dsch:
            dsch.append(ten_chuan)
    return dsch

def ghi(ds, ten_file):
    with open(ten_file, 'w', encoding='utf-8') as f:
        for ptu in ds:
            f.write(f"{ptu}\n")

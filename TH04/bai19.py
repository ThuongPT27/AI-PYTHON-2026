def thong_ke(ten_file):
    ds = []
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for dong in f:
                if ds.append(int(dong.strip()))
    except FileNotFoundError:
        return set(), 0, 0, 0
    
    if not ds:
        return set(), 0, 0, 0

    set_khong_trung = set(ds)
    so_lon_nhat = max(ds)
    so_nho_nhat = min(ds)
    gtri_tb = sum(ds) / len(ds)

    return (set_khong_trung, so_lon_nhat, so_nho_nhat, gtri_tb)

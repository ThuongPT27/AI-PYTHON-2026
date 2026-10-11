def dem(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            cac_dong = f.readlines()
            return len(cac_dong)
    except FileNotFoundError:
        return 0

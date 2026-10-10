def in_dict_dep(my_dict):
    for key, value in my_dict.items():
        print(f"{key} -> {value}")

thong_tin = {
    "Tên": "Phạm Thương",
    "Tuổi": 19,
    "Thành phố": "Hà Nội"
}

in_dict_dep(thong_tin)

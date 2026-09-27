so_kWh=int(input("Nhập số kWh tiêu thụ: "))
tong_tien=0
if 0 <= so_kWh <= 50:
    tong_tien= so_kWh* 1800
elif 51 <= so_kWh <= 100:
    tong_tien=50*1800+(so_kWh-50)*2000
else:
    tong_tien=50*1800+50*2000+(so_kWh-100)*2500
print(tong_tien)

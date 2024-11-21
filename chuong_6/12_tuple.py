luong = float(input("Nhập số lương: (VNĐ)"))
if luong < 0:
    print("số lương ko đc âm")
else:
    if luong > 15000000:
       thue = luong * 0.30
    elif luong <= 15000000 and luong >= 7000000:
        thue = luong * 0.20
    else: 
        thue = luong * 0.10
#Tính lương ròng
luong_rong = luong - thue

#In 
print(f"\nLuong: {luong:.0f} VND")
print(f"Thuế: {thue:.0f} VND")
print(f"lương ròng: {luong_rong:.0f} VND")
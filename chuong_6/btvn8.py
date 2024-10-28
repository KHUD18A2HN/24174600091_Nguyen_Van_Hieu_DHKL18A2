#bai8
diem_chuyen_can = float(input("Nhap diem chuyen can: "))
diem_giua_ki = float(input("Nhap diem giua ki: "))
diem_cuoi_ki = float(input("Nhap diem cuoi ki: "))
if diem_chuyen_can > 0 and diem_giua_ki > 0 and diem_cuoi_ki > 0:
   diem_trung_binh = (diem_chuyen_can + diem_giua_ki + diem_cuoi_ki)/3
   if diem_trung_binh >=9: 
       print("loại A ")
   elif diem_trung_binh >=7 and diem_trung_binh <9:
       print("loại B ")
   elif diem_trung_binh >= 5 and diem_trung_binh <7: 
       print("loại C ")
   elif diem_trung_binh < 5:
       print("loại D")
else:
    print("chuong trinh ko ton tai")
print("ket thuc")


#bai1
nam = float(input("Nhập năm nhuận:"))
if nam > 0:
    nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
    print(f"nam do la nam nhuan")
else:
    print(f"ket thuc")
loai_xe = input("(nhap loai xe(4 hoặc 7))")
while loai_xe not in ['4', '7']:
    print("Không hợp lệ. Vui lòng nhập loại xe(4 hoặc 7)")
    loai_xe = input("(nhap loai xe(4 hoặc 7))")
quang_duong = float(input("Nhập quãng đường đi (km): "))
thoi_gian_cho = float(input("Nhập thời gian chờ (phút): "))
if loai_xe == '4':
    cuoc = 11000 / 0.8
    if quang_duong <= 0.8:
        cuoc += 11000
    else:
        cuoc += 11000
        quang_duong -= 0.8
        if quang_duong <= 20:
           cuoc += quang_duong * 12100
        else:
            cuoc += 20 * 12100
            quang_duong -= 20
            cuoc += quang_duong * 10000
else:
    #Giá mở cửa 
    cuoc = 13000 / 0.8
    if quang_duong <= 0.8:
        cuoc += 13000
    else:
        cuoc += 13000
        quang_duong -= 0.8 
        if quang_duong <= 30:
         cuoc += quang_duong * 14100
        else:
            cuoc += 30 * 14100
            quang_duong -= 30 
            cuoc += quang_duong * 12000
#Tính tiền chờ 
if thoi_gian_cho > 5: 
    cuoc += (thoi_gian_cho - 5) * 800
print(f"Tổng cước taxi là: {cuoc:.0f} đồng")
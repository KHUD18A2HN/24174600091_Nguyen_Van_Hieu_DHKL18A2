sieu_thi = []
while True:
    print("quản lý sieu thi")
    print("Các bước: ")
    print("B1. MÃ hàng.")
    print("B2. Tên hàng.")
    print("B3. đơn vị tính.")
    print("B4. đơn giá. ")
    print("B5. số lượng")
    lua_chon = input("Hãy lựa chọn yêu cầu của bạn: ")
    if lua_chon.isdigit() == False:
        raise ValueError("Yêu cầu nhập lại.")
    else:
        lua_chon = int(lua_chon)
        if lua_chon == 1:
            ma = input("Nhập mã sp: ")
            ten = input("Nhập tên sp: ")
            don_vi = input("Nhập dơnd vị tính: ")
            don_gia = float(input("NHập đơn giá của sp: "))
            so_luong =int(input("Nhập số lượng sp: "))
    print("Thành tiền và VAT là 10%")
    thanh_tien =( don_gia*so_luong)
    print(f"Thành tiền: {thanh_tien}")
    thue = thanh_tien / 10 
    print(f"Thuế: {thue}")
    
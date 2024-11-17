#Bài tập về chuỗi ký tự 
#Dạng thứ nhất: áp dụng xử lý chuỗi ký tự bằng các phương thức có sẵn 


#Bài 1: Nhận vào 1 chuỗi ký tự bất kì. Đếm số ký tự trong chuỗi. 
#Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky:")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"so ky tu trong chuoi la {so_ky_tu_trong_chuoi}")
#Cách 2
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem + 1
print(f"so ky tu trong chuoi la {dem}")

#Bài 2: Nhập vào một chuỗi bất kỳ. Xóa các khoảng trống ở đầu và cuối chuỗi
chuoi_nhap_vao = input("Nhap vao chuoi bat ky:")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip() 
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")

#Cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
#    chuoi nhap vao          
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu  == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau = False
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu 
        
#Chuỗi nhập vào            
chuoi_dao_nguoc = chuoi_xu_ly[::-1] # type: ignore
chuoi_dao_nguoc_xu_ly_dau = ""
for chu in chuoi_dao_nguoc:
    if chu  == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau = True
        chuoi_dao_nguoc_xu_ly_dau    =     chuoi_dao_nguoc_xu_ly_dau  + chu 
chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"Chuoi sau khi xoa khoang trong {chuoi_ket_qua}")


#Bài 3: Nhập vào một chuỗi bất kỳ. Xóa tất acr các khoảng trống thừa trong chuỗi 
#VD chuoi nhap vao 
# Cách 1
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)

#chuoi nhap vao 
print(f"Chuoi ket qua: {chuoi_ket_qua}")

#Cách 2 Bài tập về nhà xử lý vòng lặp và xử lý chuỗi ký tự 

#Dạng thứ 2: áp dụng kết hợp xưr lý vòng lặp và xử lý chuỗi ký tự 
#Bài1 :Nhập vào chuỗi ký tự bất kỳ. Đêms xem có bao nhiêu ký tự là số bao nhiêu kys tự đặc biệt 
#isalpha(): Kiểm tra chữ cái 
#isdigit(): Kiểm tra số 
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0 
dem_ky_tu_dac_biet = 0 
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu = dem_chu + 1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
            
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1
            
print(f"So chu cai: {dem_chu}")
print(f"So so:{dem_so}")
print(f"so ky tu dac biet {dem_ky_tu_dac_biet}")



#Bài 2: Nhập vào số nguyên tố bất kỳ, kiểm tra xem số này có phải là số nguyên tố hay không 

n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n.isdigit():
    print("Gia tri nhap vao ko phai gia tri so nguyen duong")
#các số nhập vào phải là số nguyên dương 
#các số nguyên tố là các số lớn hơn 1
#các số nguyên tố là các số chia hết cho 1 và chính nó 

    print("so nay ko phai so nguyen to")
else:
    k = n 
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("so nay khong phai so nguyen to")
            break
        k = k - 1
    else:
        print("so nay la so nguyen to") 
        
#bài3: Nhập vào 2 số thực bất kỳ. Tính tổng 2 số thực đó 
while True:  
    a = float(input("nhap so thuc a: "))
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = a.replace("_","")
    if a.isditgit() == False:
        print("Gia tri nhap vao ko phai gia tri so")
    else:
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count(".")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("gia tri nhap khong phai gia tri so")
        else:
            vi_tri_dau_gach = a.find(".")
            if vi_tri_dau_gach != 0:
                print("gia tri nhap khong phai gia tri so")
            else:
                break
        
            
    b = float(input("nhap so thuc b: "))
    tong = a + b
    print(f"tong hai so thuc la:{tong}")

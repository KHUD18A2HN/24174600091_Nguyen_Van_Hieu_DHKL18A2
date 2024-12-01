#Bài1
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
print("Số lượng từ trong chuỗi là:", len(danh_sach_tu))

#Bài3
ho_ten = input("Nhập vào họ tên đầy đủ: ")
parts = ho_ten.split()
ho = parts[0]
ten = parts[-1]
print(f"Ho: {ho}, Ten: {ten}")
#Bài9 
chuoi_nhi_phan = input("Nhập vào chuỗi nhị phân: ")

if chuoi_nhi_phan.isdigit() and all(bit in '01' for bit in chuoi_nhi_phan):
    
    thap_phan = int(chuoi_nhi_phan, 2)
    
    print(f"{chuoi_nhi_phan} la so nhi phan, chuyen sang thap phan: {thap_phan}")
else:
    print(f"{chuoi_nhi_phan} khong phai la so nhi phan hop le!")

#Bài 10
chuoi = input("Nhập vào chuỗi ký tự: ")


so = ''.join([char for char in chuoi if char.isdigit()])
khong_so = ''.join([char for char in chuoi if not char.isdigit()])


ket_qua = so + khong_so


print("Kết quả sau khi dồn tất cả số sang bên trái:", ket_qua)

#Bài2 
chuoi = input("Nhập vào chuỗi ký tự: ")
loai_bo = ' '.join(chuoi.split())
print("Chuỗi sau khi loại bỏ dấu cách thừa:", loai_bo)


#Bài4 Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký 
chuoi = input("Nhap chuoi ky tu: ")
dem_chu_cai = 0 
dem_chu_so = 0 
dem_dac_biet = 0
for char in chuoi:
    if char.isalpha():
        dem_chu_cai += 1
    elif char.isdigit():
        dem_chu_so += 1
else:
    dem_dac_biet += 1
print(f"so ky tu la chu: {dem_chu_cai}")
print(f"so ky tu la so: {dem_chu_so}")
print(f"so ky tu la ky tu dac biet: {dem_dac_biet}")


#Bài 5 # Bài 5: Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
chuoi = input("Nhap chuoi ky tu: ")
so_chu_hoa = 0 
so_chu_thuong = 0

for ky_tu in chuoi:
    if ky_tu.isupper():
        so_chu_hoa += 1
    elif ky_tu in chuoi:
        so_chu_thuong += 1
print(f"so chu viet hoa la: {so_chu_hoa}")
print(f"so chu thuong la: {so_chu_thuong}")

#Bài 6:  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
chuoi = input("Nhap vao chuoi ky tu: ")
if chuoi.startswith('_') and chuoi.isdigit():
    print("chuoi nay la so am")
else:
    print("chuoi nay khong phai la so am")
    
# Bài 7: Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
chuoi = input("Nhap vao chuoi ky tu: ")
try:
    float(chuoi)
    if '.' in chuoi and chuoi.count('.') == 1 and chuoi.replace('.', '', 1).isdigit():
        print("chuoi nay la so thap phan")

    else:
        print("Chuỗi này không phải là số thập phân.")
except ValueError:
    print("Chuỗi này không phải là số thập phân.") 
    
# Bài 8: Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
str_1 = input("nhap vao sau ky tu str_1: ")
str_2 = input("Nhap vao xau ky tu str_2: ")

if str_2 in str_1:
    print(f"'{str_2} nằm trong '{str_1}")
if str_1 in str_2:
    print(f"'{str_1} nằm trong '{str_2}")
if str_1 not in str_2 and str_1 not in str_2:
    print(f"ko co xau ky tu nao nam trong xau ky tu kia ") 
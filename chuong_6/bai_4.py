import math

#Nhập thời gian sử dụng bóng đèn 
thoi_gian = float(input("nhap thoi gian su dung bong den(giây)"))

U = 220 
I = 2.7

#Tính tiền
tien_dien = U * I * thoi_gian * 7000 / 3600 
#In kết quả
print(("tinh_tien : ", tien_dien))


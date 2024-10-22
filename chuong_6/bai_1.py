import math 
#Nhập bán kính và chiều cao
r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao (h): "))
if h > 0 and r > 0:
    #Hằng số Pi
    pi = 3.14

    # Tính diện tích xung quanh
    s_xung_quanh = 2 * pi * r * h


    # Tính diện tích toàn phần
    s_toan_phan = 2 * pi * r * h + 2 * pi * r**2
        
    # Tính thể tích
    the_tich = pi * r**2 * h
        
    # In kết quả
    print(f"Diện tích xung quanh: {s_xung_quanh:.2f}")
    print(f"Diện tích toàn phần: {s_toan_phan:.2f}")
    print(f"Thể tích: {the_tich:.2f}")
else:
    print("r va h phai lon hon 0")
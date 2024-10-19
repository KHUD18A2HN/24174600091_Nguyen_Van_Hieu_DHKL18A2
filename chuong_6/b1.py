import math 
#Nhập bán kính và chiều cao
radius = float(input("Nhập bán kính (r): "))
height = float(input("Nhập chiều cao (h): "))
#Hằng số Pi
pi = 3.14

# Tính diện tích xung quanh
lateral_area = 2 * pi * radius * height


# Tính diện tích toàn phần
total_area = lateral_area + 2 * pi * radius**2
    
 # Tính thể tích
volume = pi * radius**2 * height
    
# In kết quả
print(f"Diện tích xung quanh: {lateral_area:.2f}")
print(f"Diện tích toàn phần: {total_area:.2f}")
print(f"Thể tích: {volume:.2f}")
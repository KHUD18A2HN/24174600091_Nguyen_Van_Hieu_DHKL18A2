import math
a = float(input("nhập giá trị a: "))
b = float(input("nhập giá trị b: "))
c = float(input("nhập giá trị c: "))
if a and b and c < 0:
    #Nhập biểu thức 
    a*x**2 + b*x + c = 0 
    #Tính delta
    delta = b**2 - 4*a*c > 0 
    #Phương trình có 2 nghiệm
    X1 = (-b - math.sqrt("delta")) / 2*a
    x2 = (-b + math.sqrt("delta")) / 2*a
    delta == b**2 - 4*a*c = 0 
    #Phương trình có nghiệm kép 
    x1 = x2 = -b / 2*a
    delta = b**2 -4*a*c < 0 
    #Phương trình vô nghiệm 
    #In ra kết quả
    print("x1, x2 là nghiệm của phương trình. ")
else:
    print("a, b, c phai la so am")
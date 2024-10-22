import math

x = float(input("nhập x : "))

s = (-x + math.sqrt(x**2 + 4)) / (x**4 +1)**(1/7)
print("kết quả là : ", round(s, 2))

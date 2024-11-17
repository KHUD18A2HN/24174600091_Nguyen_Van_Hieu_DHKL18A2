#Bài 1 Sử dụng vòng lặp for in ra màn hình các số nguyên dương lẻ nhỏ hơn 100
from xml.dom.pulldom import SAX2DOM


n = int(input("Nhập số nguyên dương: "))
for i in range(1, 100, 2):
    
    print(i)
#Bài 2 Tính các phép tính sau 
# S1 = 1 + 2 + 3 + 4 + …. + n
n = int(input("Nhập giá trị của n: "))
S1 = 0 
for i in range(1, n + 1):
    S1 += i
print("Tổng S1 =" ,S1)    
#S2 = 1*2*3*4*…*(n-1)
n = int(input("Nhập giá trị của n: "))
for i in range(1, n):
    SAX2DOM *= i
print("Tích S2 = ")
# S3 S3 = 1 – 1/2 + 1/3 – 1/4 + …. + ((-1)**n)/n
n = int(input("Nhập giá trị của n: "))
S3 = 0 
for i in range(1, n + 1):
    S3 += ((-1) ** i) / i
print("Tổng S3 =", S3)

#Bài 3 In 50 số đầufib tiên trong dãy Fibonacci 
n = 50 
fib = [0, 1]
for i in range(2, n):
    next_fib = fib[i - 1] + fib[i - 2]
    fib.append(next_fib)
for number in fib:
    print(number)
    
#Bài 4 Viết chương trình nhập vào một số kiểm tra xem số đó có phải số nguyên tố hay không? 
n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n <= 1:
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
        
        
        
      
n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n <= 1:
    print("so nay ko phai so nguyen to")
else:
    la_snt = 1
    for i in range(2, n):  
        if n % i == 0:
            la_snt = 0
            break
    if la_snt == 0:
        print("ko phai la so nt")
    else:
        print("la so nt")

  
  
  
        


#Bài5  Viết chương trình nhập vào một số kiểm tra xem số đó có phải số hoàn hảo hay không?
n = int(input("Nhập số nguyên n: "))
if n <= 0:
    print(f"không phải số hoàn hảo {n}")
else:
    tong_uoc = 0 
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += 1 
            
    if tong_uoc == n:
        print(f"là số hoàn hảo {n}")
    else:
        print("ko là só hoàn hảo {n}")
        
        
#Bài6 Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không?
n = int(input("Nhập vào một số nguyên n: "))
if n < 0:
    print(f"ko phải là số chính phương vì là số âm ")
else:
    x = 0 
while x * x < n:
    x += 1 
    
    if x * x == n:
        print(f"là số chính phương {n}")
    else:
        print(f"ko phải là số chính phương {n}")
        
        
#Bài7 Viết chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n

n = int(input("Nhập vào n: "))

for num in range(2, n):
    is_prime = True  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:  
            is_prime = False
            break  
    if is_prime:
        print(num, end=" ")  


#Bài8Viết chương trình nhập vào n, tìm tất cả các số hoàn hảo nhỏ hơn n
n = int(input("Nhập n: "))
for a in range(2, n):
    x = 0 
    for i in range(1, a):
        if a % i == 0:
            a += i 
    if x == a:
        print(a, end=" ")
        
#Bài9 Viết chương trình nhập vào n, tìm tất cả các số chính phương nhỏ hơn n
n = int(input("Nhập vào n: "))
x = 1 
while x * x < n:
    print (x * x, end=" ")
    x += 1
    
    
#Bài10 Viết achương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

x = 1 
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        x = i
        
print(f"Ước chung lớn nhất là: {x}")


#Bài11 Viết chương trình nhập vào hai số bất kì, tìm bội chung nhỏ nhất của hai số đó
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

x, y = a, b
while y != 0:
    x, y = y, x % y 
    
s = (a * b) // x 
print(f"Bội chung nhỏ nhất {a} và {b} là: {s}")


#Bài12 Viết chương trình nhập vào mẫu số và tử số của một phân số, trả về kết quả phân số đã tối giản
numerator = int(input("Nhập tử số: "))
denominator = int(input("Nhập mẫu số: "))
if denominator == 0:
    print("mẫu số ko thể bằng 0.")
else:
    a = abs(numerator)
    b = abs(denominator)
    while b != 0:
        a, b = b, a % b 
        
simplified_numerator = numerator // a
simplified_denominator = denominator // a 

print(f"Phân số đã tối giản là: {simplified_numerator}/{simplified_denominator}")
        
        
        
#Bài13 Viết chương trình nhập vào một số, trả về thừa số nguyên tố của số đó
def so(N):
   if N == 1:
        return "1"
   for i in range (2,10):
      if N % i == 0:
         a = i
         b = N // i
         return f"{a}*{so(b)}" 
print(so(18)) 

#Bài15
print("Chọn chức năng:")
print("1. Chuyển từ cơ số 10 sang cơ số 2")
print("2. Chuyển từ cơ số 2 sang cơ số 10")
choice = input("Nhập lựa chọn (1 hoặc 2): ")
if choice == "1":
    decimal = int(input("Nhập số thập phân: "))
    if decimal == 0:
        print("Số nhị phân tương ứng: 0")
    else:
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        print(f"Số nhị phân tương ứng: {binary}")
elif choice == "2":
    binary = input("Nhập số nhị phân: ")
    if all(bit in "01" for bit in binary):
        decimal = 0
        binary = binary[::-1]  
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** i
        print(f"Số thập phân tương ứng: {decimal}")
    else:
        print("Số nhị phân không hợp lệ.")
else:
    print("Lựa chọn không hợp lệ!")
    
    
    
#Bài 14
n = int(input("Nhập số hàng n: "))
print("Tam giác Pascal:")
for i in range(n):
    row = [1]
    for j in range(1, i):
        row.append(row[j - 1] * (i - j) // j)
    row.append(1) 
    print(" ".join(map(str, row)).center(2 * n))
    print("\nTam giác Floyd:")
    current_num = 1
for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(current_num))
        current_num += 1
    print(" ".join(row))
    
    
    
    
    
    
    n = int(input("Nhập số hàng cho Tam giác Floyd: "))
a = 1
# Vẽ Tam giác Floyd
for i in range(1, n + 1):
    for j in range(i):
        print(a, end=' ')
        a += 1
    print()
print("\nTam giác Pascal:")
for i in range(n):
    # In khoảng trắng để tạo hình tam giác
    print(' ' * (n - i - 1), end='')
    
    b = 1
    for j in range(i + 1):
        # In giá trị của Tam giác Pascalb
        print(b, end=' ')
        # Tính giá trị tiếp theo của Tam giác Pascal
        b = b * (i - j) // (j + 1)
    
    print()

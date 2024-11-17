#Vòng lặp trong Python 
#Vòng lặp có giới hạn (vòng lặp for)
#a
#Các kiểu dữ liệu tuần tự: string, list, tuple, set, dictiomary
#range()
#n = input()
#for i in range(10):
#    print(i) 
#range(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền giá trị mặc định yêu cầu phải là trị nguyên dương 
#range giá trị trong range sẽ chạy từ 0 đến n - 1

#Khi sử dụng vòng lặp nên kết hợp sử dụng với các câu lệnh điều kiện 
#(Khi sử sụng vòng lặp nên có mục đích rõ ràng)

#Trong python vòng lặp cung cấp chongười dùng 3 công cụ : break, continue, else
#break: Dùng vòng lặp ngay lập tức thoạt tại lần gặp break
for i in range(10):
    if i == 4:
        continue
    print(i)

#continue: Vòng lặp sẽ bỏ qua lần gặp mà ở đấy xuất hiện continue
#else: Vòng lặp sẽ chạy các câu lệnh  xử lý của else trong trường hợp 
#      vòng lặp không gặp break





#In dãy số các số lẻ nhỏ hơn n
#n = int(input("Nhập vào số nguyên dương n: "))
#for i in range(n): #-> chuỗi chạy từ 0 đến n - 1
#   if i%2 == 1:
#        print(i)
#In n các số Fibonacci
a = 0 
b = 1 
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b 
    a = b 
    b = sum_a_b
#Tính tổng các số hạng từ 1 đến n
tong_s = 0 
n = int(input("Nhập vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + 1
    print(f"tong_s = {tong_s}")
print(f"Tong cac so tu 1 den n{tong_s}")
#Tính giai thừa của số (n!)
tich_p = 1 
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    if i == 0: 
        continue
    tich_p = tich_p*1

print(f"Tich giai thua cua so n {tich_p}")
#Nhập vào 2 số a,b tìm ước chung lớn nhất của 2 dãy số này
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
so_nho_nhat = a 
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
    k = k - 1
# Kiểm tra số n  có phải số nguyên tố hay không
#số nguyen tố là số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó 

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
        
            




#Vòng lặp không giới hạn (vòng lặp while)
n = 10
while n > 2: #TRUE
    print(f"chay vong lap {n}") 
    n = n - 1

#Vòng lặp while cũng hỗ trợ break, continue và else
#Break 
n = 10
while n > 2: #TRUE
    n = n - 1
    print(f"chay vong lap {n}")
   
    if n == 6:
        break

      
#Continue   
n = 10 
while n > 2: #TRUE
    n = n - 1
   
   
    if n == 6:
        continue 
        print(f"chay vong lap {n}")
    
#Else
while n > 2:
    n = n - 1
   
   
    if n == 0:
        break
else:
        print("chay cau lenh else")
        
        
n = 10 
while n > 2: #TRUE
    n = n - 1
   
   
    if n == 6:
        continue 
else:
    print(f"chay cau lenh else")
    
    
    
    
#Tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng 20   
n = 20 
while True:
    for i in range(1, n):
        if n%i == 0 and n != 1 and i != n:
            n = n - 1
            break
    else:
       break
    
    if n < 1:
        break
        
print(f"so nguyen to la {n}")

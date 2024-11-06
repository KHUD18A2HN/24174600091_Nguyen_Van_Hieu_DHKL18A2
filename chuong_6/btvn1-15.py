#Bài 1 Sử dụng vòng lặp for in ra màn hình các số nguyên dương lẻ nhỏ hơn 100
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
    S2 *= i
print("Tích S2 =", S2)
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
        
        
        
#Bài5  Viết chương trình nhập vào một số kiểm tra xem số đó có phải số hoàn hảo hay không?

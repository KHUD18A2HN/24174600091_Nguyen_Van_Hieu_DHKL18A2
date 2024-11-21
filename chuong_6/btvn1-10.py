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
        
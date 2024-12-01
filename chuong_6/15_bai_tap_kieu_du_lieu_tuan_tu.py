#Bài 1: Nhập vào số nguyên dương n. 
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
ds_nguyen_to = []
while True:
    n = input("nhap vao so nguyen duong: ")
    if n.isdigit() == False:
        print("Yeu cau lại so nguyen duong!!")
    else:
        n = int(n)
        break 
    
for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)
        
        
ds_nguyen_to.sort()
print(ds_nguyen_to)



#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    
    n = input("nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau lại so nguyen duong!!")
    else:
        n = int(n)
        break 
    
for i in range(n):
    while True:
     so = input(f"Nhap gia tri so {i + 1}")
    if so.isdigit() == False:
        print("Yeu cau lại so !!")
    else:
        n = int(so)
        break 
    ds_so.append(so)
    
tong = sum(ds_so)
print(f"tong cac so vua nhap: {tong}")





#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần

n = int(input("Nhập số nguyên dương n: "))

A = []
B = []

for i in range(1, n):
    if i % 2 == 0:
        B.append(i)  
    else:
        A.append(i) 


A.sort(reverse=True)
B.sort(reverse=True)


print("Danh sách A (số lẻ nhỏ hơn n):", A)
print("Danh sách B (số chẵn nhỏ hơn n):", B)

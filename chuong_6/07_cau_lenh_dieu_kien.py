#Câu lệnh điều kiện 
#3 kiểu viết câu lẹnh điều kiện 
#câu lệnh if...(sử dụng với 1 điều kiện xét)
#câu lệnh if...else... (sử dụng với 1 điều kiện cần xét và có điều kiện
# #câu lệnh if...else... (sử dụng với nhiều điều kiện cần xét)
#xử lý xoay quoanh boolean (True , False)
1 < 2
1 > 2
1 >= 2
1 <= 2
1 != 2
"abc" == "123"
#=> trở về kết quả True hoặc False
#Đối với if khi xét điều kiện 
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động 
# - Nếu điều kiện sai (False) thì câu lệnh của if sẽ hoạt động 
a = 10 
if a > 20: 
    print("Gia tri a thoa man dieu kien")
    b = a + 1
print("ket thuc chuong trinh")

#Đối vơi if...else khi xét điều kiện 
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động 
# - Nếu điều kiện sai (False) thì câu lệnh của if sẽ hoạt động 
a = 10 
if a > 5: 
    print("gia tri a thoa man")
else:
    print("gia tri a khong thoa man")
print("Ket thuc chuong trinh")       
#Đối với if...elif...else
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động 
# - Nếu điều kiện sai (False) thì câu lệnh của if sẽ hoạt động 
#       + Nếu điều kiện của elif đúng (True)        
#       + Nếu điều kiện của elif đúng (False)
a = 10
if a > 0: 
    print("a la so duong")
elif a < 0:
    print("a la so am")
else:
    print("a la so 0")

print("Ket thuc chuong trinh")


            
a = []
b = ["abc", 1, 5, 6.7, []]

a = 5 
b = a + 1
print(a)
print(b)

a = ["abc", "def", "ghijk", 1, 2, 3]
b = a 
b[0] = "chuoi thay doi"
print(a)
print(b)


#Phương thức sao lưu 
a = ["abc", "def", "ghijk", 1, 2, 3]
b = a.copy()
b[0] = "chuoi thay doi"
print(a)
print(b)

#Thay đổi giá trị trong danh sách 
a = ["abc", "def", "ghijk", 1, 2, 3]
a[3] = 10 
a[1:4] = [6, 7, 8]
print(a)

#Độ dài danh sách
print(len(a))
#Các phương thức thêm và bớt 
#thêm cuối danh sách 
a.append("abca")
a.append([1,2,3])
print(a)
#Thêm nhiều phần tử
a.extend([1,2,3])
print(a)

#Xóa tất cả các phânnf tử trong danh sách 
#a.clear()
#Lâys phần tử cuối cùng ra khỏi danh sách 
b = a.pop()
print(a)
print(b)

#Xóa 1 phần tử trong chuỗi 
a.remove("abc")

#Thêm 1 phần tử vào vị trí index
a.insert(3, "kkk")

#Dếm số phần tử xuất hiện 
a.count("abc")

#Đảo ngược danh sách 
a.reverse()
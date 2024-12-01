#sét - Tập hợp trong python 
#Tính chất của tập hợp 
#-Không có sắp xếp,  không có thứ tự 
#Những phầnn tử trong tập hợp là đặc hiệu (unique)
# Các giá trị trong set có thể thay đổi đc tuy nhiên nó chỉ có thể chứa các phần tử mang giá trị ko đổi

list_a = ["fol", "baa", "baal"]

set_a = {1,2,2,"abc"}
set_b = set(list_a) 

#Kiểm tra số phần tử trong tập hợp 
len(set_a)
#Kiểm tra phần tử có tồn tại trong tập hợp không 
2 in set_a #=> trả về kiểu dữ liệu boolean : True

if 2 in set_a:
    print("2 co trong tap hop")
    
2 not in set_a  #=> trả về kiểu dữ liệu boolean : True

if 2 in set_a:
    print("2 ko co trong tap hop")

#Kiểm tra so sánh 2 tập hợp 
#Tập hợp A
tap_hop_a = {"a", "b",1,2,3}
#Tập hợp B
tap_hop_b = {1, 2, 3,"a", "b"}

#Kiểm tra tập A có phải tập con của B ko 
tap_hop_a.issubset(tap_hop_b) #=> tả về kiểu dữ liệu boolean
tap_hop_a < tap_hop_b   
tap_hop_a <= tap_hop_b

#Kiểm tra tập A có phải tập con của B ko 
tap_hop_a.issubset(tap_hop_b)
tap_hop_a > tap_hop_b   
tap_hop_a >= tap_hop_b

#Kiểm tra xem 2 tập hợp này có giao nhau hay ko
tap_hop_a.isdisjoint(tap_hop_b) #Trả về True nếu ko có phần tử chung và False nếu có 
tap_hop_a != tap_hop_a < tap_hop_b   
tap_hop_a <= tap_hop_b

#Các tính toán trong tập hợp 
#Tập hợp A
tap_hop_a = {"a", "b", "c", "d"}
#Tập hợp B
tap_hop_b = {1, 2, 3,"a", "b"}
#Tập hợp C 
tap_hop_c = {1,2,3,4,5,6}

#Phép tập hơpj  
tap_hop_tong = tap_hop_a.union(tap_hop_b)
tap_hop_tong = tap_hop_a.union(tap_hop_b).union(tap_hop_c)
tap_hop_tong = tap_hop_a | tap_hop_b | tap_hop_c

#Phép láY phầm giao giữa các tập hợp 
tap_hop_tong = tap_hop_a.intersection(tap_hop_b)
tap_hop_tong = tap_hop_a.intersection(tap_hop_b).intersection(tap_hop_c)
tap_hop_tong = tap_hop_a & tap_hop_b & tap_hop_c

#Phép lấy phần tử trong 1 tập hợp mà không có trong các tập hợp còn lại 
tap_hop_khac = tap_hop_a.difference(tap_hop_b)
tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c

#Phép lấy hợp của phần có trong tập hợp này mà không có trong tập hợp kia 
tap_hop_giao = tap_hop_a.symmetric_difference(tap_hop_b)
tap_hop_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
tap_hop_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c

#Chỉnh sửa tập hợp
tap_hop_a = {1,2,3}
tap_hop_a = {"a","b","c"}

#Thêm phần tử a 
tap_hop_a.add(9)
tap_hop_a.update([4,5,6]) #Tương tự với việc hơn 2 tập hợp 
# a = 1
# b = 2 
# a += b 
#a = a + b 
tap_hop_a = tap_hop_b | tap_hop_b
tap_hop_a |= tap_hop_b
 
#Giữ lại các phần tử là giao cuar 2 tập hợp 
tap_hop_a.intersection_update(tap_hop_b)
tap_hop_a = tap_hop_a - tap_hop_b
tap_hop_a -= tap_hop_b 

#Giữ lại các phần tử ko tồn tại trong cả 2 tập hợp 
tap_hop_a.symmetric_difference_update(tap_hop_b)
tap_hop_a = tap_hop_a - tap_hop_b
tap_hop_a ^= tap_hop_b

#XÓa phần tử trong tập hợp 
#Xóa 1phần 
tap_hop_a.remove(2)
#xÓa nhiều phần tử 
tap_hop_a.difference_update({1,2})
#xóa phần tử ko gây lỗi 
tap_hop_a



#lấy 1 phần tử bât kỳ ra để sd và xóa phần tử này khỏi tập hợp 
tap_hop_a.pop()
#xóa toàn bộ 
tap_hop_a.clear()

tap_hop = ["a", "b", "c", "d", "e"]
while tap_hop:
    a = tap_hop.pop()
    print(a)
    
    
    
    
    
    
    
    
    
#Từ điển trong python
#-Lưu trữ các kiểu dữ liệu khác 
#-Có thể thay đổi các giá trị trong từ điền 
#Có thể luu các kiểu dữ liệu tuần tự khác tạo thành mạng lưới 
#-Không sử dụng các giá trị phải truy cập bằng khóa 
tu_dien  = {"abc":1,
            3:[1,2,3],
            (0,1):"hijk"}
#khai báo từ điển 
#- Từ điển sử dụng hoặc {} để khởi tạo 
#-Mỗi phần tử phải theo cặp khóa: giá trị 
#-Khóa trong từ điển phải là các giá trị ko thể thay đổi 
#-Khóa ko đc giống nhau 
list_a = [(0, "Hoang"),(1, "Cuong")]
tu_dien_a = dict(list_a)
#Từ điển trong Python có cách hoạt động giống như JSon 

#Truy cập các phần tử trong từ điển 
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["a"]
#Lấy các giá trị khóa 
tap_hop_khoa = tu_dien.keys()
#Lấy danh sách giá trị 
danh_sach_gia_tri = list(tu_dien.values())
#lấy danh sách các cập khóa giá trị 
danh_sach_khoa_gia_tri = list(tu_dien.items)

#Thêm giá trị vào trong từ điển 
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}

tu_dien["d"] = 4 

tu_dien.update({"e", 5})
print(tu_dien)
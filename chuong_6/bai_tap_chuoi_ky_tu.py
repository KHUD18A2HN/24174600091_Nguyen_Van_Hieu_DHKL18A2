#Bài1
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
print("Số lượng từ trong chuỗi là:", len(danh_sach_tu))

#Bài3
ho_ten = input("Nhập vào họ tên đầy đủ: ")
parts = ho_ten.split()
ho = parts[0]
ten = parts[-1]
print(f"Ho: {ho}, Ten: {ten}")



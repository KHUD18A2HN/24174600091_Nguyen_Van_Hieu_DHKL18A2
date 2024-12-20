#Đọc ghi file
#C:\Users\PC\Documents\24174600091_Nguyen_Van_Hieu_DHKL18A2\file_a.txt
#file_a.txt
#folder_upload\file_a.txt
open_file= open(file="file_a.txt", mode="r")
#r: chỉ đọc file từ đầu đến cuối, nếu tệp tin không tồn tại sẽ 
#r+: đọc và ghi tệp tin từ dòng đầu đến cuối, nếu tệp tin ko tồn tại
#w: mở và ghi tệp tin (ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#w+: đọc và ghi tệp tin(ghi đè), nếu tệp tin không tồn tại, tạo tệp tin mới
#a: mở và ghi vào cuối tệp tin, nếu tệp tin không tồn tại báo lỗi
#a+: đọc và ghi tệp tin, nếu tệp tin không tồn tại báo lỗi
print(open_file.readline(),end="")
print(open_file.readline(),end="")
print(open_file.readline(),end="")
open_file.close()

write_file = open(file="file_a.txt", mode="w")
write_file.write("chuoi thong tin moi")
write_file.writelines(["dong1\n","dong2\n","dong3\n"])
write_file.close()


with open(file="file_a.txt", mode="r") as open_file:
    list_text=open_file.readlines()
    
for i in list_text:
    print(i)
    
list_text_copy=list_text.copy
list_text.append("dong4\n")
list_text.append("dong5\n")
list_text.append("dong6\n")
list_text_copy[2]="dong3\n"
with open(file="file_a.txt", mode="w") as write_file:
    write_file.writelines(list_text_copy)
    
    
import csv
with open(file="book.csv, mode="r"") as open_file:
          csv_reader = csv.reader(open,delimiter=",")

csv_file = list(csv_reader).copy()
for row in csv_file:
    print(row)
    
with open(file="book.csv, mode="w"") as write_file:
    csv_write = csv.writer(write_file)
    csv_write

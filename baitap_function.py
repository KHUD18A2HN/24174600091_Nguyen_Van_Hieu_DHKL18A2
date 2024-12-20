#Bai_1 Viết hàm kiểm tra chuỗi ký tự có phải số nguyên 
def is_integer(s):

    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return True
    return False


print(is_integer("123"))   
print(is_integer("-123"))  
print(is_integer("12.3"))  
print(is_integer("abc"))   


#Bai_2 Viết hàm kiểm tra chuỗi ký tự có phải số nguyên dương
def is_positive_integer(s):
   
    if s.isdigit() and int(s) > 0:
        return True
    return False


print(is_positive_integer("123"))  
print(is_positive_integer("0"))    
print(is_positive_integer("-123")) 
print(is_positive_integer("12.3"))
print(is_positive_integer("abc"))  

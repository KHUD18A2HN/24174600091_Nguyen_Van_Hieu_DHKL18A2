def f():
    s = '-- Inside f()'
    print(s)
    
print('Before calling f()')
f()
print('After calling f()')


def f(qty, item, price):
    print(f'{qty}, {item}, cost ${price:.2f}')
f(6, 'bananas', 1.74)
    
    
def kiem_tra_so_nt(x):
    

    if x < 2:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
    


def tinh_trung_binh(*args):
   #KIểm tra giá trị trong args
   tong = 0 
   for i in args
        tong = tong + i
    trung_binh = tong/len(args)
    


list_ttsv = []
def nhap_thong_tin_sv(**kwargs):
    #Kiểm tra cac gia gia trong kwargs
    if kwargs["diem_tb"] >= 7:
        kwargs["lop"] = A1
    elif kwargs["diem_tb"] >= 4:
        kwargs["lop"] = A2 
    list_ttsv.append(kwargs)
    pass 

nhap_thong_tin_sv(ten="Hieu", tuoi="18", diem_tb="6.0")







def tinh_tong_hai_so(a: int = 1, b: int = 2) -> float:
    """
    Hầm tính toán nhận vào hai số a và b \n
    Trả về tổng hai số này
    """
    return a + b
tinh_tong_hai_so(4,5)

print("avc")
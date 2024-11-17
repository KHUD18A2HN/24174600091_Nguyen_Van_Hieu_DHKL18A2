import math 
x = float (input("Nhap gia tri x: "))
if x > 0:   

   f_x = math.log(x , 4) + math.log(2 , x)  
    
   print(f"Gia tri can tim f(x) = {f_x:.2f}") 
else:   
    print("x phai lon hon 0")

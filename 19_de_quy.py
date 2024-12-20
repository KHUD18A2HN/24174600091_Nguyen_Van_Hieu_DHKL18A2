#Đệ quy - Recursion - sự tái lập 

#Ví dụ: Dãy fibonacci
#0 + 1 = 1
#1 + 1 = 2
#1 + 2 = 3
#2 + 3 = 5 
#3 + 5 = 8
#5 + 8 = 13 
#....

#Số tiếp theo = số hiện tại + số trước đó
#F1 = 2 
#F2 = 3
#F3 = F1 + F2 = 2 + 3 = 5
#F(n)=F(n-1) + F(N-2) => Đệ quy trên toán học 

#Đệ quy trong lập trình là các hàm có lợi gọi chính nó trong nội hàm 
def f():
    f()
#=> Hàm đệ quy hoạt động 


def so(N):
   if N == 1:
        return "1"
   for i in range (2,10):
      if N % i == 0:
         a = i
         b = N // i
         return f"{a}*{so(b)}" 
print(so(18))
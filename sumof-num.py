
n=int(input("enter the num"))

def sumofn(n):
   
   if n<=0:
      return 0
   else :
      return n + sumofn(n-1)
   
result=sumofn(n)
print(result)




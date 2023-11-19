# doubt

n=int(input("enter the num"))

def sumofn(n):
   
   if n<=0:
      return 0
   else :
      return n + sumofn(n-1)
   
result=sumofn(n)
print(result)




# def starprinting(n):
#     pattern = ''
#     for i in range(n):
#         line = '*' * (n - i)
#         pattern += line + '\n'
#         print(line)
#     return pattern

# n = int(input("Enter the number of rows: "))
# result = starprinting(n)
# print("Pattern of asterisks:\n", result)


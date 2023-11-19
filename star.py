# doubt


n=int(input("enter the num"))
def starprinting(n):
    if n>0:
        for i in range(n):
         print('*'*(n-i))
x=starprinting(n)
print(x)




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


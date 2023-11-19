# * * * * 
# * * *
# * *
# *


# 1  2  3  
# 1  2
# 1

n=int(input("enter number of rows:"))
for i in range (n):
    print("* " * (n-i))


n=int(input("enter number of rows:"))
for i in range (n):
    for j in range (n-i):
        print((j+1) ,end="  ")
    print() 
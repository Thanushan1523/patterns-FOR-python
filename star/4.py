
#  1 
#  2 2
# 3 3 3


# n=int(input("enter number of rows:"))
# for i in range (n):
#     print(" "*(n-i-1) + (str(i+1)+" ") *(i+1))


# pyramid number patteren with fixed num in rows


# DOUBT I HAVE TO MAKE A NESTED LOOP FOR ABOVE 
n=int(input("enter number of rows:"))
for i in range (n):
    print(" "*(n-i-1), end='') 
    for j in range (i+1):
           print(n-j,end=" ") 

    print()   
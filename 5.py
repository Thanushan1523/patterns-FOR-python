# PYRAMID PATTERN WITH ALPHABET SYMBOLS IN REVERESE OF DICTONARY
#   D 
#   D C
#  D C B
# D C B A
n=int(input("enter number of rows:"))
for i in range (n):
    print(" "*(n-i-1), end='') 
    for j in range (i+1):
           print(chr(64+n-j),end=" ")
    print()    


n=int(input("enter number of rows:"))
for i in range (n):
   
    for j in range (i+1):
           print(chr(65+j),end=" ")
    print()    
for i in range (n-1):
   
    for j in range (n-i-1):
           print(chr(65+j),end=" ")
    print()

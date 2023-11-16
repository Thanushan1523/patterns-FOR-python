# iverted pyramid pattern with alphabet symbol in dictonary order in every row
n=int(input("enter number of rows:"))
for i in range (n):
   
    for j in range (n-i):
           print(chr(65+j),end=" ")
    print()    

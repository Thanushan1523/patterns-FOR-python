# print("hi")

# print ("hellow")
# n=int(input("enter number of rows:"))
# for i in range (n):
#     print("*" )
 

# for i in range (n):
#     print("*" ,end="")

# for i in range (n):
#     print("*" ,end=" ")


# n=int(input("enter number of rows:"))
# for i in range (n):
#     print("* " *n )


# n=int(input("enter number of rows:"))
# for i in range (n):
#     print(str(n)  *n )


# n=int(input("enter number of rows:"))
# for i in range (n):
    
#     print(str(i+1) *n )




# n=int(input("enter number of rows:"))
# for i in range (n):
#     print("A " *n )


# n=int(input("enter number of rows:"))
# for i in range (n):
#     print((chr(65+i)+" ") *(i+1) )


# n=int(input("enter number of rows:"))
# for i in range (n):
#     print("* " * (n-i))


# n=int(input("enter number of rows:"))
# for i in range (n):
#     for j in range (n-i):
#         print((j+1) ,end="  ")
#     print() 


# pyramid number patteren with fixed num in rows
# n=int(input("enter number of rows:"))
# for i in range (n):
#     print(" "*(n-i-1) + (str(i+1)+" ") *(i+1))


# DOUBT I HAVE TO MAKE A NESTED LOOP FOR ABOVE 
# n=int(input("enter number of rows:"))
# for i in range (n):
#     print(" "*(n-i-1), end='') 
#     for j in range (i+1):
#            print(n-j,end=" ") 

#     print()   


# PYRAMID PATTERN WITH ALPHABET SYMBOLS IN REVERESE OF DICTONARY

# n=int(input("enter number of rows:"))
# for i in range (n):
#     print(" "*(n-i-1), end='') 
#     for j in range (i+1):
#            print(chr(64+n-j),end=" ")
#     print()    


# n=int(input("enter number of rows:"))
# for i in range (n):
   
#     for j in range (i+1):
#            print(chr(65+j),end=" ")
#     print()    
# for i in range (n-1):
   
#     for j in range (n-i-1):
#            print(chr(65+j),end=" ")
#     print()

# # iverted pyramid pattern with alphabet symbol in dictonary order in every row
# n=int(input("enter number of rows:"))
# for i in range (n):
   
#     for j in range (n-i):
#            print(chr(65+j),end=" ")
#     print()    

n=int(input("enter number of rows:"))
for i in range (n):
    print(" " * i,end=" " )
    for j in range (n-i):
           print(chr(65+j),end=" ")
    print()    

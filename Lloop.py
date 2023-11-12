# a=[5,5,9,4,8,6]
# i=0
# while i < len(a):
#     print(a[i])
#     i=i+1




# for loop
# i=1
# while i<13:
#     print("2*",i , "=", 2*i)
#     i=i+1


# n=3
# for i in range(n):
#     for j in range(n):
#         if j==0 and j==2:
#              print("*",end="")
#         else:
#             print(" ")




# # 
# num=int(input("enter your num:"))

# for i in range (2,num):
#     if num % i==0 :
#         print( num,"is not prime number")
#         break
# else:
#     print(num , "is prime number")



# # import math

# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     if n <= 3:
# #         return True
# #     if n % 2 == 0 or n % 3 == 0:
# #         return False
    
# #     i = 5
# #     while i * i <= n:
# #         if n % i == 0 or n % (i + 2) == 0:
# #             return False
# #         i += 6

# #     return True

# # # Test the is_prime function
# # number = int(input("Enter a number: "))
# # if is_prime(number):
# #     print(number, "is a prime number.")
# # else:
# #     print(number, "is not a prime number.")


# num=int(input("enter your num:"))
# sum=0
# i=0
# while i <num+1:
#     sum=sum+i
#     i=i+1
# print(sum)


# num=int(input("enter your num:"))
# sum=0
# i=1
# while i <num+1:
#     sum=sum+i
#     i=i+2
#     print(sum)
    
# num=int(input("enter your num:"))
# count=0
# sum=0
# i=1
# while count <num:
#     sum=sum+i
#     count=count+1
#     i=i+2
#     print(sum)
# num=int(input("enter your num:"))
# sum=0
# i=2
# while i <num+1:
#     sum=sum+i
#     i=i+2
#     print(sum)

# n=int(input("enter your num:"))
# for i in range(n+1):
#     print("*" *i)
n=int(input("enter your num:"))
for i in range(n+1):
    print(" "*(n-i-1),"* " *(i+1))


# n=int(input("enter number of rows:"))
# for i in range (n):
    
#     print(str(i+1) *n )











# from datetime import datetime
# a=int(input ( "enter the first value:"))
# b=int(input ( "enter the second value:"))

# # def add(a,b):
# #     ans=a+b
# # print(a+b) 
# print(a%2)

# c=5
# print (type(c))

# a=5
# b=8
# if a>b:
#     print("a is grater than b")
# else :
#     print("b is grater than a")


# ave=(a+b)/2
# print(ave)

# square=(a**2)
# print(square)


# a=[2,3,5,8,10,15]

# print(a[0:3])

# name= ("r","k","g","r","u")

hi="tha  nsu"
# print(len(hi))
# name=input("enter your name:")
# today=datetime.now()
# print("good afternoon", name,"\n", today)

# if "  " in hi:
#     print("space")
# else:
#     print("no space")


# print(hi.replace( '  ' , ' '))

# countspace=hi.count(" ")
# print(countspace)


# list1 = [1,5,6,8,9]
# list1[2:4]=[20,25]
# print(list1)

# list1.clear()
# print(list1)

# fruits= [  ]
# fruits=(input("type your fruits"))
# print (fruits)


fruits = []
for i in range(7):
    fruits.append(input(f"Name of Fruit {i+1}:  "))
print(fruits)



# fruits = []
# for i in range(7):
#     fruit = input("enter your marks:  ")
#     fruits.append(fruit)
#     fruits.sort()

# print(fruits)

# list=[2,5,3,1]
# sum=0
# for i in list:
#     sum +=i

# print(sum)


# list=[7,0,8,0,0,9]
# print(list.count(0))
      
    
# a=set()
# a.add(1)
# a.add(2)
# print(a)



set1={1,2,4,5,6,8,10}
set2={2,5,1,6,8,}
set3=set1.union(set2)
set4=set1.intersection(set2)
print(set4)

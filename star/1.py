
# * * *
# *   *
# * * *




n=int(input("enter number of rows:"))
for i in range(n):
    if i == 1:
        print("*   *")
    else:
        print("* " * n)

n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(n):
        if i == 1 and  j == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
x = int(input("Enter the number of rows is "))
for i in range(1,x+1):
    for j in range(x-i):
        print("",end="  ")
    for k in range(i):
        print(i,end= " ")
    for l in range(i-1):
        print(i,end=" ")
    print("")

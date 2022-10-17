lower =int(input("enter lower range:"))
upper =int(input("enter upper range:"))
print(f"Perfect numbers between {lower} and {upper} :")
for num in range(lower, upper):
    temp = num
    sum = 0
    for i in range(1, temp):
        if(temp % i == 0):
            sum = sum + i
    if (sum == num):
        print(num)

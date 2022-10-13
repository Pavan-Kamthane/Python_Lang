# Python program to determine whether
# the number is Armstrong number or not

def power(x, y):
	
	if y == 0:
		return 1
	if y % 2 == 0:
		return power(x, y // 2) * power(x, y // 2)
		
	return x * power(x, y // 2) * power(x, y // 2)


def order(x):

	n = 0
	while (x != 0):
		n = n + 1
		x = x // 10
		
	return n

def isArmstrong(x):
	
	n = order(x)
	temp = x
	sum1 = 0
	
	while (temp != 0):
		r = temp % 10
		sum1 = sum1 + power(r, n)
		temp = temp // 10

	return (sum1 == x)


x = 153
print(isArmstrong(x))

x = 1246
print(isArmstrong(x))

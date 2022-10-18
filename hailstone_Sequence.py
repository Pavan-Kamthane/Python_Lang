hailstone_list = []
def hailstone(n):
  hailstone_list.append(int(n))
  if n == 1:
    return hailstone_list
  while n != 1:
    if n % 2 == 0:
      return hailstone(int(n/2))
    else:
      return hailstone(int(3*n + 1))
 
n = int(input("Enter the number:"))
hailstone_list = []
hailstone_list = hailstone(n)
print("Hailstone Sequence for n = {} is : {}".format(n, hailstone_list)) 
print("Number of steps is : ",len(hailstone_list))

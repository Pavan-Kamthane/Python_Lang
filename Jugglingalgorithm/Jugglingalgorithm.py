import math
def leftRotate(arr, d, n): 
     for i in range(math.gcd(d, n)): 
         temp = arr[i] 
         j = i 
         while 1: 
             k = j + d 
             if k >= n:
                 k = k - n 
             if k == i: 
                 break
             arr[j] = arr[k] 
             j = k 
             arr[j] = temp 
arr =list(map(int,input("ENTER ARRAY ELEMENTS ").split()))
n = len(arr)
no_of_rotations = 2

print("Array Elements before rotation : ")
print(*arr) 
leftRotate(arr, no_of_rotations, n )
print("\nArray Elements after rotation : ")
print(*arr)

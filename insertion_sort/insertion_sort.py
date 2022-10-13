
def InsertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


l = []
print("Enter the size of array: ")
a = int(input())
for i in range(a):
    n = random.randint(1, 100)
    l.append(n)

InsertionSort(l, a)
print(l)

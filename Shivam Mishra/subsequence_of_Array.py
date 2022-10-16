def subsequenceArray(ind,n,arr,list1):
    # Base Condition
    if(ind==n):
        for i in list1:
            print(i,end=" ")
        if(len(list1)==0):
            print("{}")
        print("\n")
        return
    # Pick the element
    list1.append(arr[ind])
    # increase index by 1 and call function
    subsequenceArray(ind+1,n,arr,list1)
    #when base condition occur for uper recursion return and Clear the list
    list1.pop()
    # call next recursion
    subsequenceArray(ind+1,n,arr,list1)
   
list1=[]
arr=[3,1,2]
n=len(arr)
subsequenceArray(0,n,arr,list1)

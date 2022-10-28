def stair(n):
    # base condition
    if(n==1):
        return 1
    if(n==2):
        return 2
    # recuesive call
    call1=stair(n-1)
    call2=stair(n-2)
    # samll calculation
    smallcal=call1+call2
    return smallcal

n=int(input("Input the stair no.you want to reach: "))
s=stair(n)
print(s)

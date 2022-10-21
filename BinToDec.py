def binaryToDecimal(n):
     
    ans, i =  0, 0
    while(n != 0):
        digit = n % 10
        ans = ans + digit * pow(2, i)
        n = n//10
        i += 1
    print(ans)   
     
 
# Driver code
if __name__ == '__main__':
    val = int(input("Enter a binary number: "))
    binaryToDecimal(val)
    
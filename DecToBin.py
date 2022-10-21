def DecimalToBinary(n):
     
    ans, i =  0, 0
    while(n != 0):
        bit = n&1
        ans = ans + bit * pow(10, i)
        n = n>>1
        i += 1
    print(ans)   
     
 
# Driver code
if __name__ == '__main__':
    val = int(input("Enter a decimal number: "))
    DecimalToBinary(val)
    
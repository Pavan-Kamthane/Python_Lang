def check(s):
    s1=s[::-1]
    if(s==s1):
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")
    m=s[0:len(s)//2]
    n=s[len(s)//2::]
    if(m==n):
        print("The given string is Symmetric")
    else:
        print("The given string is not symmetric")
s=input("Enter the string:")
check(s)

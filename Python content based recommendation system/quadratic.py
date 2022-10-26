import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")

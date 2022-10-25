def pattern(n):
   for i in range(n):
      for j in range(n):
         # printing stars
         print("* ",end="")
      print("\r")
 
# take inputs
n = int(input('Enter the number of rows: '))

# calling function
pattern(n)

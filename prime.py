def fibonacci_recursion(my_val):
   if my_val <= 1:
      return my_val
   else:
      return(fibonacci_recursion(my_val-1) + fibonacci_recursion(my_val-2))
num_terms = 12
print("The number of terms is ")
print(num_terms)
if num_terms <= 0:
   print("Enter a positive integer...")
else:
   print("The Fibonacci sequence is :")
   for i in range(num_terms):
      print(fibonacci_recursion(i))

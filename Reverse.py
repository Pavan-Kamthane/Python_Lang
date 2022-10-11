# the number to be reversed
num = 529412

# the number after reversal
reversed_num = 0

# start a while loop till complete number has been reversed
while num != 0 :
    
    # taking modulo with 10 gives us the last digit of num
    curr_digit = num % 10
    
    # appending the last digit of num to reversed_num
    # for this we multiply the curr reversed_num by 10 and add curr_digit to it
    
    reversed_num = 10*reversed_num 
    reversed_num = reversed_num + curr_digit
    
    # remove the last digit from num by dividing it by 10
    num = num // 10
    
# we get the reversed_num
print("Reversed Number is: " + str(reversed_num))

num = int(input('Enter number: '))

a, b = 0, 1
i = 0

if num <= 0:
    print('Please enter a positive integer.')

elif num == 1:
    print('The Fibonacci series: ')
    print(a)

else:
    print('The Fibonacci series: ')
    while i < num:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        i = i+1

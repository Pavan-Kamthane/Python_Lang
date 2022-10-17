print('\x1b[1;37;45m' + '----------------------------------------------'  + '\x1b[0m')
print('\x1b[1;37;45m' + ' Showing all prime numbers within an interval '  + '\x1b[0m')
print('\x1b[1;37;45m' + '----------------------------------------------'  + '\x1b[0m')
print('\n')

lower = 0
upper = 0

while upper <= lower:
    lower = int(input('Enter lower number: '))
    upper = int(input('Enter upper number: '))
    print('\n')

    if upper > lower:
        print('\x1b[5;30;42m' + ' Prime numbers between', lower, 'and', upper, 'are: ' + '\x1b[0m')

        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
    else:
        print('\x1b[0;37;41m' + '** Upper must be greater than Lower! **' + '\x1b[0m')
        print('\n')

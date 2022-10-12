def print_fibonacci(num):
    print(f"Fibonacci series for first {num} numbers: ", end=" ")
    x, y = 0, 1
    if num == 1:
        print(x)
    elif num == 2:
        print(x, y)
    else:
        print(x, y, end=" ")
        for i in range(3, num+1):
            x, y = y, x+y
            print(y, end=" ")


if __name__ == "__main__":
    try:
        n = int(input("Please enter an integer to print first n Fibonacci numbers"))
        if n == 0:
            raise ValueError('0 not a valid input')
        print_fibonacci(n)
    except ValueError as e:
        print("Rerun the program")

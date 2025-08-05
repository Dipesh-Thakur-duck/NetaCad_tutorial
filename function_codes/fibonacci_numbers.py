def fib(n):
    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    else:
        value1 = 1
        value2 = 1

        for i in range(3, n + 1):
            result = value1 + value2
            value1 = value2
            value2 = result
        return result
value = int(input("Enter a number: "))
print(f"Fibonacci number of {value} is {fib(value)}")
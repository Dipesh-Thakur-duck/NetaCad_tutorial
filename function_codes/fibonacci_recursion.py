def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# fib(4) -> 3 (2 + 1) = fib(3) + fib(2) -> 2 + 1
value = int(input("Enter a natural number: "))
print(f"Fibonacci number when value = {value} is {fib(value)}")
         
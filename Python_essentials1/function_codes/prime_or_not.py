# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.

def prime_or_not(value):
    counter = 0

    for i in range(1, value + 1):
        if value % i == 0:
            counter += 1
    if counter < 2:
        return False
    elif counter > 2:
        return False
    return True

value = int(input("Enter a natural number: "))
result = prime_or_not(value)

if result:
    print(f"{value} is a prime number")
else:
    print(f"{value} is not a prime number")
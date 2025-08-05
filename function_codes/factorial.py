# Factorial of a number is the product of all positive numbers less than or equal to it 
# There are no factorials for numbers below 0
# 0! = 1 and 1! = 1

input = int(input("Enter a number you want factorial of: "))

def factorial(input):
    if input < 0: 
        return None
    if input < 2:
        return 1
    product = 1

    for i in range(2, input + 1):
        product *= i
    return product

print(f"Factorial of {input} is {factorial(input)}")
largest_number = -999999
number = int(input("Enter a number or -1 to exit: "))

while number != -1:
    if number > largest_number: largest_number = number
    number = int(input("Enter a number or -1 to exit: "))
print(f'Greatest number is {largest_number}')
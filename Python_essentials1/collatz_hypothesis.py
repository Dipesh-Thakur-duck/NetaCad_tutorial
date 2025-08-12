n_negative_0 = int(input("Enter a positive integer: "))
if n_negative_0 <= 0:
    print("Please enter a number greater than 0.")
else:
    steps = 0
    while n_negative_0 != 1:
        if n_negative_0 % 2 == 0:
            n_negative_0 //= 2
        else:
            n_negative_0 = 3 * n_negative_0 + 1
        print(n_negative_0)
        steps += 1
    print("Total steps:",steps)
    

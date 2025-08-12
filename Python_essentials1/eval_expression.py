x = float(input('Enter a number:'))
print(f"Output of a really complex expression with x:{x} is ",end="")
y = 1 / (x + (1 / (x + (1 / (x + (1/x))))))
print(y)
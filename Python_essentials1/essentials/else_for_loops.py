# Runs only if the loop completes normally (no break is hit)

numbers = [1, 2, 3]

for n in numbers:
    if n == 4:
        print("Found 4!")
        break
else:
    print("4 not found")

# Output -> 4 not found
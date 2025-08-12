"""
1. ** (binding right to left)
2. *, /, //, %
3. +, -
"""
# binding determines the order of computations performed by some operations with equal priority, put side by side in one expression

x = 2**3**2 # output: 512 unlike 64
print(x)

ex_1 = 6/4
ex_2 = 6//4 #rounds the decimal down to closet integer
ex_3 = 6 % 4

print(f"Normal division:{ex_1}",f"Floor division: {ex_2}",f"Modulus Operator: {ex_3}",sep="\n")



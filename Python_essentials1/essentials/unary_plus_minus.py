# unary plus and minus have highest priority (more than any arithmetic operators or conditional operators)

# Unary '-' negates the value

positive_num = int(input("Enter a positive number: "))
print(-positive_num)

# Unary '+' does nothing and do the following

print(+True) # -> 1
print(+False) # -> 0
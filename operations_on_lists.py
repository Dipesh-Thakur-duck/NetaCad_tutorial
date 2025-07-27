# The innner life of lists
# Example:

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2) # -> [2]

# In list, the variable name is the name of the memory location where the list is stored.

# list_2 = list_1 copies the memory location not its content. Hence modifying one of them affects the other, and vice versa.

# Solution: Slice
# Syntax: [start:stop:step]

list_1 = [1,2,3,4]
list_2 = list_1[:] # -> produces an exact copy of list_1 for list_2
print(list_2)

list_3 = list_1[1:3] # slice list_1 from 1 to end - 1
print(list_3)

# negative indices are possible so we can use them in slice

list_4 = list_1[:-1] # -> basically start from 0 and reach the end - 1 as -1 is the las element and its excluded
print(list_4) 

del list_1[:2] # -> removes elements as per slice instruction when 'del' keyword is used
print(list_1)

list_1 = ["A","B","C"]
list_2 = list_1
list_3 = list_2

del list_1[0] # -> affects the actual list
del list_2 # -> basically removes the pointer to the list

print(list_3) # -> ["B","C"]
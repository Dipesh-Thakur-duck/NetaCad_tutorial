# tuples 

# Creating tuples
tuple_1 = (1,2,3,4)
tuple_2 = 1,2,3,4

print(type(tuple_2))

# tuple with single value

tuple_s = (1,)
tuple_s1 = 1,
number = (1) # -> just a number in a paranthesis, not a tuple

print(type(number)) # -> int
print(type(tuple_s), type(tuple_s1))

empty_tuple = ()

# same as list
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:]) # -> (10, 100, 1000)
print(my_tuple[:-2]) # -> (1, 10)
print(my_tuple[::-1]) # -> (1000, 100, 10, 1)

for elem in my_tuple:
    print(elem)

# what else can tuples do?

my_tuple1 = (1, 10, 100)

t1 = my_tuple + (1000, 10000) # the '+' operator can join tuples together

t2 = my_tuple * 3 # the '*' operator can multiply tuples

print(len(t2)) # the len function accepts tuples, and returns the number of elements contained inside

print(t1)
print(t2)
print(10 in my_tuple1)
print(-10 not in my_tuple1)

# tuples elements can be anything from variables and integer to string and literals

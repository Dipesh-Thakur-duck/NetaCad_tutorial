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

# you can't delete the individual elements of a tuple but you can delete the whole tuple

tuple1 = (1,2,3)
del tuple1
# print(tuple1) -> creates a NameError

# built-in function: tuple()

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

# index method
my_list = (1,2,0,10)
print(my_list.index(0)) # -> 2
print(my_list.index(10,2)) # -> starts searching 10 from index 2 onwards
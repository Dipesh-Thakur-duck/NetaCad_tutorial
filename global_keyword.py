# The scope of a name is the part of a code where the name is properly recognizable.

def my_function():
    print("Do I know that variable?", var)

var = 1
my_function() 

# since var is created before function call, it is recognized inside the funciton

# a variable existing outside a function has scope inside the function's body

print(var)

def my_function1():
    var = 2 
    print("Do I know that variable?", var) # 

var = 1
my_function1()

# A variable existing outside a function has scope inside the function's body, excluding those which define a variable of the same name

# It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). 


print(var)

def my_function2(var): # var only takes the value of var variable outside the block of my_function2
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function2(var)
print(var)

def my_function3():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function3()

# 'global' keyword extends a variable's scope in a way which includes the function's body so any value is reflected globally rather than creating a new variable

print(var)

def my_function4(n):
    print("I got", n)
    n+=1
    print("I have", n)

var = 1
my_function4(var)
print(var)

# changing the parameter's value doesn't propagate outside the function
# This also means that a function receives the argument's value, not the argument itself. This is true for scalars
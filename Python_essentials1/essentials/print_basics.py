# print function
print("Hello World!")

# print function with multiple argruments
print("Hello World!", "It's a pleasure to be here.") #sep = " "

# print function with single quotation and multi-line string
print('This is inside single quotation')
print('''I
am
a
multi-line
string.''')

#print function with end and sep argument
print("Hello world!","It's nice to be here.",sep="-",end="*")

print() #- acts as a newline special character

#print function with escape character- allows use to add special characters into the string
name = "Dipesh Thakur"
print(f"Hello \"{name}\". It's a pleasure to have you.")

def sum(arg1,arg2):
    """Gives you the sum"""
    return arg1 + arg2

print(sum(1,2))
# Dictionary is not a sequence type and it is mutable

# The list of pairs is surrounded by curly braces, while the pairs are separated by commas and key and values by colons

dictionary = {"cat":"chat","dog":"chien", "horse":"cheval"}
phone_numbers = {"boss": 123, "Samir": 456}
empty_dictionary = {} # -> empty dictionary

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# a key may be any immutable type of ojbect: it can be a number or even a string, but not a list

dict_1 = {(1,):"one"}
print(dict_1[(1,)])

# a dictionary is a one-way tool: key -> value, value X key

# dictionary can't be browsed using for loop since it's not a sequence type but we have simple and very effective tools that can helps us

# The keys() method

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# The items() method

for key, value in dictionary.items():
    print(key, "->", value)

# Modifying and adding values

dictionary['cat'] = 'minou' # -> modifying
print(dictionary)

# Adding values
dictionary['swan'] = 'cygne'
dictionary.update({"duck":"canard"})

# sorting
for key in sorted(dictionary.keys()):
    print(key, '->', dictionary[key])

# removing a key:value pair

del dictionary["cat"]
print(dictionary)
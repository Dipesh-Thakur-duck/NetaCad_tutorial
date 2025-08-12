dict1 = {
    1:"One",
    2:"Two"
}
dict2 = {
    3:"Three",
    4:"Four"
}
dict3 = {}
for item in (dict1,dict2):
    dict3.update(item)

print(dict3)
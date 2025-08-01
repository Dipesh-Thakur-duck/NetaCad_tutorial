list_1 = [1,2,3,4,5]

# in and not in are two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or no.

print(5 in list_1)
print(12 not in list_1)
print(0 in list_1)

# finding the greatest number from list

# way 1
my_list = [1,2,3,4,5]
greatest = my_list[0]

for i in range(len(my_list)):
    if greatest < my_list[i]:
        greatest = my_list[i]

print(greatest)

# way 2

my_list1 = [12,1,15,17,-1,0,5]
greatest1 = my_list1[0]

for i in my_list1:
    if i > greatest1:
        greatest1 = i

print(greatest1)

# more efficient

my_list2 = [1,2,3,5,18,12,13]
greatest3 = my_list2[0]

for i in my_list2[1:]:
    if i > greatest3:
        greatest3 = i
print(greatest3)
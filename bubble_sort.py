list1 = [1,5,10,3,2]
swapped = True

while swapped:
    swapped = False
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            swapped = True

print(list1)


# Quick and easy

list2 = [1,2,10,3,4]
list2.sort() # ascending order
print(list2) 
list2.sort(reverse=True) # descending order
print(list2)

# reverse()
list3 = [1,2,4,3,6]
list3.reverse() # descending order
print(list3)
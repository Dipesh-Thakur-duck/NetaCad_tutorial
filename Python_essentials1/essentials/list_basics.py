list1 = [1,2,3,4,5,'end'] # use square brackets to declare list

print(len(list1)) # to know the number of elements in a list

list1[5] = 6 # can change the elements in a list

del list1[1] # this will delete the second element in the list, del is an instruction not a function

print(f'Length of list: {len(list1)} and list: {list1}') # You will get length one less than previously and the element at second place is deleted

print(list1[-1]) # negative indices are legal and -1 will give us the element at last

# Adding elements to a list: append() and insert()

# append() takes its argument's value and puts it at the end of the list
dummy_list = [1,2,3,4,5]
dummy_list.append(6)
print(dummy_list) # [1,2,3,4,5,6]


#insert() method can add a new element at any place in the list

# insert(index, value)
dummy_list.insert(0,0)
print(dummy_list) # [0,1,2,3,4,5,6]

hat_list = [1,2,3,4,5,6]

user_input = int(input("Enter a integer value:"))

hat_list[len(hat_list)//2] = user_input # change the element at the middle of the list

del hat_list[-1] # delete the element at the end of the list

print(len(hat_list),hat_list)
# List comprehensions

# A list comprehension is actually a list, but created on-the fly during program execution, and is not described statically

# Example:

list_1 = []
for i in range(10):
    list_1.append(i ** 2)
print(list_1)

# List comprehension version
list_2 = [x ** 2 for x in range(10)]
print(list_2)

# syntax: [<task> for loop]

# produce a ten-element list filled with first eight powers of two

list_3 = [2 ** i for i in range(10)]
print(list_3)

# creating a 64 cell chess board 

EMPTY = None
board = [[EMPTY for i in range(8)] for j in range (8)]

# An automatic weather station the records air temprature hourly throughout the month
import random

temps = [[f"{random.uniform(-10.0, 40.0):.2f}" for h in range(24)] for d in range(31)]

# to determine the average monthly noon temparature

total = 0.0

for day in temps:
    total += float(day[11])

average = total / 31
print(f"Average temperature at noon: {average:.2f}")

# to determine the highest temprature during the whole month
highest = -100
for day in temps:
    for temp in day:
        if float(temp) > highest:
            highest = float(temp)
print(f"The highest temperature was: {highest:.2f}")

# count the days when the temprature at noon was at least 20

days = 0
for day in temps:
    if float(day[11]) > 20:
        days += 1
print(f"There were {days} days when temperature was at least 20")

# It's a hotel. 3 buildings, 15 floors and 20 rooms on each floor.

rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]

rooms[1][9][13] = True # booking room 13 in floor 9 of building 1

rooms[2][4][1] = True # booking room 1 in floor 4 of building 2

vacancy = 0

for room in range(20):
    if not rooms[1][9][room]:
        vacancy += 1

print(vacancy)

# if there's an else statement, for loop comes after the if-else statement

# if there's only an if block, for loop comes before the if statement

# Example:

items = [2,3,4,5]
print([item ** 2 if item % 2 == 0 else item ** 3 for item in items])

print([num ** 2 for num in [2,3,4,5] if num % 2 == 0])

# Interesting:

my_list = [[0,1,2,3] for i in range (2)] # -> creates a 2-D list with [0,1,2,3] as element at index 0 and 1
print(my_list)
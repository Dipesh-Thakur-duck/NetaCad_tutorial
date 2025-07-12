hour = int(input("Starting time (hours): ")) % 24

mins = int(input("Starting time (minutes): ")) % 60

dura = int(input("Event duration (minutes): "))

dura_hours = dura // 60
dura_mins = dura % 60

total_mins = mins + dura_mins
carry_hours = total_mins // 60
mins_final = total_mins % 60

hour_final = (hour + dura_hours + carry_hours) % 24

print(hour_final,':',mins_final,sep="")
"""
1. 'hour' variable is ensured to fall in the (0..23) range
2. 'minutes' variable is ensured to fall in the (0..59) range
3. dura_hours gives the number of hours in the dura input.
4. dura_mins gives the number of hours in the dura input.
5. total_mins calculates the total mins and if its more than 59, carry_hours is > 0
6. hour_final gives the hour value through (hour + dura_hours + carry_hours) modulu 24
7. mins_final gives the mins value through total_mins modulu 60
"""

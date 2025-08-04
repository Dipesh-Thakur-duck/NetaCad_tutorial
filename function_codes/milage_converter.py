# liters per 100 km into miles per gallon
# Formula = 235.215 / liters
# 100km = 100 / 1.609344 = 62.137 miles
# 1 liter = 1 / 3.785411784 gallon
# Say we have 3.9 liters per 100km then
# 62.137 * 3.785411784 / 30 will give the result 

def liters_100km_to_miles_gallon(liters):
    return 235.215 / liters
    
def miles_gallon_to_liters_100km(miles):
    return 235.215 / miles
     
liters = float(input("How much fuel is consumed in 100km: "))
miles = float(input("How many miles is travelled in a gallon: "))

print(f"{liters} liters / 100km is {liters_100km_to_miles_gallon(liters):.2f} miles / gallon ")

print(f"{miles} miles / gallon is {miles_gallon_to_liters_100km(miles):.2f} liters / 100km")

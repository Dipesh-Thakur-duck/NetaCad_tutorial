distance = float(input("Enter a distance:"))
unit = input("Enter a unit(mile-m/km): ")

if unit == 'm':
    print('Distance in km:', str(round(1/1.61 * distance,2)) + 'km')
elif unit == 'km':
    print('Distance in miles:', str(round(distance * 1.61,2)) + 'miles')
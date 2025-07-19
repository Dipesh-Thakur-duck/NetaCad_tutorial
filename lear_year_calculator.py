year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calender period")
else:
    if year % 4 != 0:
        print("Common year")
    else:
        if year % 100 != 0:
            print("Leap year")
        else:
            if year % 400 != 0:
                print("Common year")
            else:
                print("Leap year")
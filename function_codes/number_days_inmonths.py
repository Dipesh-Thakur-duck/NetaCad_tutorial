from leap_year_function import leap_year

test_years = []
test_months = []

while True:

    test_years.append(int(input("Enter a year: ")))
    test_months.append(int(input("Enter a month in that year: ")))

    decision = input("Do you want to know days in a month of any other year (y/n): ").lower()
    
    if decision == 'n':
        break

def days_in_month(year, month):
    result = []
    leap_year_result = leap_year(year)

    days_in_month_common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(len(leap_year_result)):
        if leap_year_result[i] == 'Gregorian calendar started from 1582':
            result.append('Befor gregorian calender started')
        elif leap_year_result[i]:
            result.append(days_in_month_leap[month[i]-1])
        else:
            result.append(days_in_month_common[month[i]-1])
    return result

result = days_in_month(test_years, test_months)

for i in range(len(test_years)):
    if result[i] == 'Befor gregorian calender started':
        print("Please make sure the year is from 1582 to beyound")
    else:
        print(f"In month {test_months[i]} of year {test_years[i]}, there were {result[i]} days")


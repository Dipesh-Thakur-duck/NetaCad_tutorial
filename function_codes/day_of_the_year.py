from number_days_inmonths import days_in_month
from leap_year_function import leap_year

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day of month: "))

def day_of_year(year, month, day):
    days = []
    result = 0
    for i in range(month - 1):
        days.append(days_in_month([year],[i]))
    for lists in days:
        for number_of_days in lists:
            result += number_of_days
    return result + day
print(f"In year {year}, day {day} of month {month} is day number {day_of_year(year,month,day)} of the year")
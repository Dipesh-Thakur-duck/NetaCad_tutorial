from leap_year_function import leap_year

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
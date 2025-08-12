def leap_year(list_years):
    result = []
    for year in list_years:
        if year < 1582:
            result.append('Gregorian calendar started from 1582')
        else:
            if year % 4 != 0:
                result.append(False)
            else:
                if year % 100 != 0:
                    result.append(True)
                else:
                    if year % 400 != 0:
                        result.append(False)
                    else:
                        result.append(True)
    return result
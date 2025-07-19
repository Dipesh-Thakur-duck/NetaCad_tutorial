def proper_format(tax):
    """Print values properly in thaleras and cents"""
    thalers = int(tax)
    cents = round((tax - thalers) * 100)
    print(f"{thalers} thalers and {cents:02d} cents")

income = float(input("Enter your income this year: "))

if income > 0:
    if income <= 85528:
        tax = (0.18 * income) - 556.02
        proper_format(tax)
    else:
        tax = 14_839.02 + (income - 85528) * 0.32
        proper_format(tax)
else:
    print("No tax leived")

# d -> means integer (decimal) format
# 2 -> means minimum width is 2 digits
# 0 -> means pad with leading zerso if it's leass than 2 digits
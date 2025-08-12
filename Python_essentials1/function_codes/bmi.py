def lb_kg(weight):
    return weight * 0.45359237

def ft_inches_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

decision = input("Imperial(I) or Metric(M) system: ").lower()

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return "Invalid input"
    return weight / height ** 2

if decision == 'i':

    weight = float(input("Enter the weight: "))
    height = float(input("Enter your height in ft: "))

    ft = int(height)
    inch = height - ft

    result = bmi(weight = lb_kg(weight), height = ft_inches_m(ft, inch))

    print(f"When weight is {weight}lb and height is {ft + inch:.2f}ft, bmi = {result}")

else:

    weight = float(input("Enter the weight: "))
    height = float(input("Enter the height: "))

    result = bmi(weight, height)

    print(f"When weight is {weight}kg and height is {height}m, bmi = {result}")
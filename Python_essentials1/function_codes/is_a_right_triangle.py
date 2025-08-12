from is_triangle import is_triangle

def is_a_right_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return False
    if a > b and a > c:
        return a**2 == b**2 + c**2
    elif b > a and b > c:
        return b**2 == a**2 + c**2
    else:
        return c**2 == a**2 + b**2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
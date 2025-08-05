from is_triangle import is_triangle

def heron(a,b,c):
    perimeter_half = (a + b + c) / 2
    return (perimeter_half*(perimeter_half - a)*(perimeter_half - b)*(perimeter_half - c))**(1/2)

def area_triange(a,b,c):
    if is_triangle(a,b,c):
        return heron(a,b,c)
    return None

print(area_triange(1,2,2.5))
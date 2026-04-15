
def rect_area(len, br):
    return len * br

def rect_perimeter(len, br):
    return 2 * (len + br)

def circle_area(rad):
    return 3.14159 * rad * rad

def circle_circumference(rad):
    return 2 * 3.14159 * rad

if __name__ == '__main__':
    print("rect_area() - ", rect_area(1, 2))
    print("rect_perimeter() - ", rect_perimeter(1, 2))
    print("circle_area() - ", circle_area(1))
    print("circle_circumference() - ", circle_circumference(1))

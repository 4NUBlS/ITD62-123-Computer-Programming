def calculate_circle_area(radius):
    PI = 3.14
    area = PI * (radius * radius)
    print("Circle radius {0}, area is {1}".format(radius,area))

def calculate_circle_circumference(radius):
    PI = 3.14
    circumference = 2 * PI * radius
    print("Circle radius {0}, circumference is {1}".format(radius,circumference))

def calculate_retangle_area(wide,length):
    area = wide * length
    print("Retangle area of {0}X{1} is {2}".format(wide,length,area))

def calculate_triangle_area(base,high):
    area = 0.5 * base * high
    print("Tritangle area of {0}X{1} is {2}".format(base,high,area))
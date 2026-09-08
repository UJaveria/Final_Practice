# Write area_of_triangle(base, height) that returns the area

def area_of_triangle(base, height) :
    area = (1 * base * height) / 2
    return area


base = float(input("Enter base triangle : "))
height = float(input("Enter height of triangle : "))
print(area_of_triangle(base, height))
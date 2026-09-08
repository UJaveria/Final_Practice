#  Create a Circle class with radius; add methods area() and circumference().
class Circle :
    def __init__(self,radius):
        self.radius = radius

    def area(self) :
        return f"Area of Circle : {3.14 * self.radius ** 2}"

    def circumference(self) :
        return f"Circumference : {2 * 3.14 * self.radius}"

# c1 = Circle(4)
# print(c1.area())
# print(c1.circumference())
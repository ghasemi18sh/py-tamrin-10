class Shape:
    def __init__(self):
        self.per = 0
        self.Area = 0
class Rectangle(Shape):
    def __init__(self, leng, br):
        Shape.per = (leng + br) * 2
        Shape.Area = leng * br
    def show_per(self):
        return Shape.per
    def show_area(self):
        return Shape.Area
class Circle(Shape):
    def __init__(self, rad):
        Shape.per = (rad * 2) * 3.14
        Shape.Area = (rad * rad) * 3.14
    def show_per(self):
        return Shape.per
    def show_area(self):
        return Shape.Area
r = Rectangle(2, 3)
print(f"{r.show_per()}   {r.show_area()}")
c = Circle(1 / 3.14)
print(f"{c.show_per()}   {c.show_area()}")
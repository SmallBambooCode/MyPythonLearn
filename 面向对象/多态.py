class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length

    def area(self):
        return pow(self.length, 2)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * 3.14


s = Square(5)
print(s.length)
print(s.area())
c = Circle(2)
print(c.name)
print(c.area())

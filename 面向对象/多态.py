# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("正方形")
#         self.length = length
#
#     def area(self):
#         return pow(self.length, 2)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("圆形")
#         self.radius = radius
#
#     def area(self):
#         return pow(self.radius, 2) * 3.14
#
#
# s = Square(5)
# print(s.length)
# print(s.area())
# c = Circle(2)
# print(c.name)
# print(c.area())

# 自定义函数实现多态接口
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是一只猫，一只快乐星猫~今年{self.age}岁，你可以叫我{self.name}")

    def say(self):
        print("喵喵喵？")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是一只修狗~今年{self.age}岁，你可以叫我{self.name}")

    def say(self):
        print("哇哇哇~")


class Turtle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是一只小黄缘龟，今年{self.age}岁，你可以叫我{self.name}")

    def say(self):
        print("龟龟不会叫！")


def animal(obj):
    obj.intro()
    obj.say()


c1 = Cat("快乐星猫", 5)
d1 = Dog("金毛毛", 3)
t1 = Turtle("小甲鱼（bushi", 10000)
animal(c1)
animal(t1)
animal(d1)

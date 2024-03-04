from abc import ABCMeta, abstractmethod
class Fruit(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    # 必须实现@abstractmethod装师的方法
    @abstractmethod
    def good_for_health(self):
        pass

class Apple(Fruit):
    # 如果不重写抽象基类中的方法就会报错
    def good_for_health(self):
        print("一天一苹果，医生远离我！")


a1 = Apple("Apple")
a1.good_for_health()

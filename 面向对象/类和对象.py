class Cube:
    r = 0

    def get_r(self):
        return self.r

    def set_r(self, new_r):
        self.r = new_r

    def get_volume(self):
        return pow(self.r, 3)


c1 = Cube()
c1.set_r(5)
print(c1.get_r())
print(c1.get_volume())
# 通过对不存在的属性进行赋值进而为对象新建属性
c1.v = c1.get_volume()
c2 = Cube()
print(c1.v)
print(dir(c1))
print(dir(c2))

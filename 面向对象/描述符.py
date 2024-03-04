# class D:
#     def __get__(self, instance, owner):
#         print("__get__")
#         print(f"self->{self}\ninstance->{instance}\nowner->{owner}")
#
#     def __set__(self, instance, value):
#         print("__set__")
#         print(f"self->{self}\ninstance->{instance}\nvalue->{value}")
#
#     # 不要与__del__混淆
#     def __delete__(self, instance):
#         print("__delete__")
#         print(f"self->{self}\ninstance->{instance}")
#
#
# class C:
#     # 让描述符D拦截x属性
#     x = D()
#
#
# c = C()
# c.x = 250
# print(c.x)
# del c.x

# class D:
#     def __get__(self, instance, owner):
#         return instance._x
#
#     def __set__(self, instance, value):
#         instance._x = value
#
#     def __delete__(self, instance):
#         del instance._x
#
#
# class C:
#     def __init__(self, x=250):
#         self._x = x
#
#     x = D()
#
#
# c = C()
# print(c.x)
# c.x = 500
# print(c.__dict__)
# del c.x
# print(c.__dict__)

# class MyProperty():
#     def __init__(self, fget=None, fset=None, fdel=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         self.fset(instance, value)
#
#     def __delete__(self, instance):
#         self.fdel(instance)
#
#
# class C:
#     def __init__(self):
#         self._x = 250
#
#     def getx(self):
#         return self._x
#
#     def setx(self, value):
#         self._x = value
#
#     def delx(self):
#         del self._x
#
#     x = MyProperty(getx, setx, delx)
#
#
# c = C()
# print(c.x)
# c.x = 500
# print(c.__dict__)
# del c.x
# print(c.__dict__)

# class MyProperty():
#     def __init__(self, fget=None, fset=None, fdel=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         self.fset(instance, value)
#
#     def __delete__(self, instance):
#         self.fdel(instance)
#
#     def getter(self, func):
#         self.fget = func
#         return self
#
#     def setter(self, func):
#         self.fset = func
#         return self
#
#     def deleter(self, func):
#         self.fdel = func
#         return self
#
# class D:
#     def __init__(self):
#         self._x = 250
#
#     @MyProperty
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x
#
#
# d = D()
# print(d.x)
# d.x = 500
# print(d.__dict__)
# del d.x
# print(d.__dict__)

# class D:
#     def __get__(self, instance, owner):
#         print("__get__")
#
#
# class C:
#     x = D()
#
#
# c = C()
# print(c.x)
# c.x = "SmallBamboo"
# print(C.x)

# class D:
#     def __get__(self, instance, owner):
#         print("__get__")
#
#     def __set__(self, instance, value):
#         print("__set__")
#
# class C:
#     x = D()
#
#     def __getattribute__(self, name):
#         print("__getattribute__")
#
# c = C()
# print(c.x)

# class D:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print("__get__")
#         return instance.__dict__.get(self.name)
#
#     def __set__(self, instance, value):
#         print("__set__")
#         instance.__dict__[self.name] = value
#
#
# class C:
#     x = D()
#
#
# c = C()
# print(c.x)
# print(c.__dict__)
# c.x = 500
# print(c.__dict__)
# print(c.x)

# class C:
#     def func(self, x):
#         return x
#
#
# c = C()
# print(c.func)
# print(C.func)

class MethodType:
    def __init__(self, func, obj):
        self.__func__ = func
        self.__self__ = obj

    def __call__(self, *args, **kwargs):
        func = self.__func__
        obj = self.__self__
        print("小白")
        return func(obj, *args, **kwargs)


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            print("旺财")
            cls = type(obj)
        if hasattr(type(self.f), "__get__"):
            print(f"来福，type(self.f) -> {type(self.f)}")
            return self.f.__get__(cls, cls)
        return MethodType(self.f, cls)


class D:
    @ClassMethod
    # @property
    def __doc__(cls):
        return f"from class {cls.__name__}"


d = D()
print(d.__doc__)

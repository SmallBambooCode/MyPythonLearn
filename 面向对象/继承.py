# class User:
#
#     # 构造函数
#     def __init__(self, username="UNKNOWN", password="UNKNOWN"):
#         self.username = username
#         self.password = password
#
#     def __delete__(self, instance):
#         pass
#
#     def set_username(self, username):
#         self.username = username
#         return self
#
#     def set_password(self, password):
#         self.password = password
#         return self
#
#     def check_info(self, username, password):
#         if username == self.username and password == self.password:
#             return True
#         else:
#             return False
#
#     def get_type(self):
#         return "UNKNOWN"
#
#
# class Root(User):
#
#     def get_type(self):
#         return "Root"
#
#
# # # 检测一个类是否为另一个类的子类
# # print(issubclass(Root, User))
# # # 打印对象属性
# # print(user1.__dict__)
#
# user1 = Root("Jerry", "2023AI")
# print("【管理员登录系统】")
# iUserName = input("请输入用户名：")
# iPassword = input("请输入密码：")
# if user1.check_info(iUserName, iPassword) and user1.get_type() == "Root":
#     print("登陆成功")
# else:
#     print("登陆失败，用户名与密码不匹配或您不是管理员")

# # 钻石继承
# class A:
#
#     def __init__(self, t=0):
#         self.t = t
#         print("A")
#
#
# class B1(A):
#
#     def __init__(self):
#         # super().__init__()
#         A.__init__(self)
#         print("B1")
#
#
# class B2(A):
#
#     def __init__(self):
#         # super().__init__()
#         A.__init__(self)
#         print("B2")
#
#
# class C(B1, B2):
#
#     def __init__(self):
#         # super().__init__()
#         B1.__init__(self)
#         B2.__init__(self)
#         print("C")
#
#
# test = C()
# print(C.mro())
#


# Mix-in类
class Displayer:
    def display(self, message):
        print(message)


class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        # 追加模式
        with open(filename, "a") as f:
            f.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="subclasslog.txt")


subclass = MySubClass()
subclass.display("This is a test.")

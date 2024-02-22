# # 普通的文件操作
# f = open("test.txt", "w")
# f.writelines(["早生耗，\n", "美丽的清晨，", "把美好的心情，\n", "送给在做的每一位新老朋友。\n"])
# f.close()
# # 使用with语句和上下文管理器
# with open("test.txt", "w") as f:
#     f.writelines(["早生耗，\n", "美丽的清晨，", "把美好的心情，\n", "送给在做的每一位新老朋友。\n"])
#

# # 序列化
# import pickle
#
# x, y, z = 1, 2, 3
# s = "Hello World"
# l = [114514, "10086", ["SmallBamboo.cn", 2005]]
#
# with open("save.pkl", "wb") as f:
#     pickle.dump(x, f)
#     pickle.dump(y, f)
#     pickle.dump(z, f)
#     pickle.dump(s, f)
#     pickle.dump(l, f)


# 反序列化
import pickle

with open("save.pkl", "rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)
    s = pickle.load(f)
    l = pickle.load(f)

print(x, y, z)
print(s)
print(l)


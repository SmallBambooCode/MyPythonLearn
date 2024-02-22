# f = open("test.txt", "w")
# f.write("I love SmallBamboo\n")
# f.writelines(["早生耗，\n", "美丽的清晨，", "把美好的心情\n", "送给在做的每一位新老朋友\n"])
# f.close()

# f = open("test.txt", "r+")
# # 检测文件对象是否可读写
# print(f.readable())
# print(f.writable())
# for each in f:
#     print(each, end="")
#
# print(f.tell())
# f.seek(0)
# print(f.read())
# f.close()

# from pathlib import Path
# print("当前工作目录：{}".format(Path.cwd()))
# # 创建路径对象
# path_obj = Path("E:/PR")
# print(path_obj)
# # 路径拼接
# path_obj = path_obj / "项目"
# print(path_obj)

from pathlib import Path
# 创建路径对象
path_obj = Path("E:/PR")
# 路径拼接
path_obj = path_obj / "项目"
# 判断路径是否为文件夹，文件
print(path_obj.is_dir())
print(path_obj.is_file())
# 测试路径是否存在
print(path_obj.exists())

p = path_obj
path_obj = path_obj / "高考加油.zip"

# 获取路径最后一部分
print(path_obj.name)
# 获取文件名
print(path_obj.stem)
# 获取后缀名
print(path_obj.suffix)
# 获取父级目录（最后一部分的前面所有内容）
print(path_obj.parent)
# 获取其逻辑祖先路径构成的序列
print(path_obj.parents)
print(list(path_obj.parents))
# 将路径拆分为元组
print(path_obj.parts)
# 查询文件/文件夹的信息
print(path_obj.stat())
# 将相对路径转换为绝对路径
print(Path("../../../../03_学习资料").resolve())
# 获取当前路径下的所有子文件和子文件夹（返回生成器）
print("XXXXX获取当前路径下的所有子文件和子文件夹（返回生成器）XXXXX")
for i in p.iterdir():
    print(i)

# 使用列表推导式和上面学习到的内容
# 将p路劲对象下的所有文件的路径保存到列表
print("XXXXX将p路劲对象下的所有文件的路径保存到列表XXXXX")
l = [x for x in p.iterdir() if x.is_file()]
for i in l:
    print(i)


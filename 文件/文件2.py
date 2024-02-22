# from pathlib import Path
# path_obj = Path("E:/PR/项目/newFolder")
# # 创建文件夹（加入exist_ok=True参数则不会因为已存在而报错）
# # 如果路径中有多个不存在的目录也会报错，parents=True参数可解决。
# path_obj.mkdir(exist_ok=True, parents=True)
# # 打开文件
# p = path_obj
# path_obj = path_obj / "好好好.txt"
# f = path_obj.open("r")
# for each in f:
#     print(each, end="")
#
# f.close()
# # 给文件/文件夹修改名字
# path_obj.rename(p / "不好不好不好.txt")

# from pathlib import Path
# path_obj = Path("E:/PR/项目/newFolder/不好不好不好.txt")
# # 删除文件
# path_obj.unlink()
# # 删除文件夹
# path_obj.parent.rmdir()

from pathlib import Path
path_obj = Path("E:\PR\项目")
# 查找文件/文件夹（返回生成器）
# ans = path_obj.glob("*.zip")
# for each in ans:
#     print(each)
#
# ans = path_obj.glob("./2024.01.17-铭凡迷你主机简单测评+踩坑分享-UM480 XT-秋竹源/*.jpg")
# for each in ans:
#     print(each)

ans = path_obj.glob("**/*.jpg")
for each in ans:
    print(each)

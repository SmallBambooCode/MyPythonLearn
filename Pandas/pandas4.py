import pandas as pd

# 读取csv文件，会自动加入索引
# data = pd.read_csv('Students.csv')
data = pd.read_pickle('Students.pickle')
print(data)

# 保存为pickle
data.to_pickle('Students.pickle')
# 保存为csv
data.to_csv('Students2.csv', encoding='utf-8-sig')
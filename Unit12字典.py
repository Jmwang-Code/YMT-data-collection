# 字典  键值对成对出现
# key是唯一的
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1['Name']: ", dict1['Name'])
print("dict1['Age']: ", dict1['Age'])

# TODO 使用大括号定义字典
dict2 = {}
# TODO 使用dict函数定义字典
dict3 = dict()

# 增改 删
dict1['Age'] = 8  # 更新
print("dict1['Age']: ", dict1['Age'])
dict1['School'] = "菜鸟教程"  # 添加
print("dict1['School']: ", dict1['School'])
del dict1['Name']  # 删除
print("dict1: ", dict1)

# len()
print(len(dict1))

# keys()
print(dict1.keys())

# values()
print(dict1.values())

# items()
print(dict1.items())
for key, value in dict1.items():
    print(key, value)

# for in key和value
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)


# clear()
dict1.clear()
print(dict1)

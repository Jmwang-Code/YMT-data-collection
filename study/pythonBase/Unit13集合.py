# 集合 ：大括号包围元素，元素通过逗号隔开 。默认是去重的
# TODO 对应java中的set
# 定义方式
s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 3, 4, 5])

# 判空
print(1 in s1)

# 增
s1.add(6)
print(s1)

# 改
s1.update([7, 8, 9])
print(s1)

# 删 删除指定的数据 如果不存在就报错
s1.remove(8)
print(s1)

# pop 移除首位
s1.pop()
print(s1)

# discard 移除指定元素 如果不存在
s1.discard(9)
print(s1)

# 交集 &
print(s1 & s2)

# 并集 |
print(s1 | s2)

# 补集 ^
print(s1 ^ s2)

# 清空
s1.clear()
print(s1)


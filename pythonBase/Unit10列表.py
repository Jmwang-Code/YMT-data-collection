# 列表
# TODO 类似java中数组，但是时间复杂度围绕O(N)左右的
'''
Python中的列表和Java的数组有一些相似之处，但也有一些重要的区别。

相似之处：
- 列表和数组都可以用于存储多个元素。
- 两者都可以通过索引访问和操作元素。
- 列表和数组都可以进行迭代和循环遍历。

不同之处：
- 列表在Python中是一种内置的数据结构，而Java的数组是一种原生的数据类型。
- TODO 列表可以容纳不同类型的元素，而Java的数组要求所有元素具有相同的数据类型。
- 列表的大小可以动态调整，可以添加、删除和修改元素，而Java的数组的大小是固定的，无法改变。
- 列表提供了许多内置的方法和功能，如添加元素、扩展列表、排序等，而Java的数组的功能较为有限。

希望以上信息对您有所帮助！如果您有任何其他问题，请随时向我提问。
'''
# 列表可以容纳不同类型的元素
name = 'TOM'
list = [1, 2, 3, '4', 5.6, 6, 7, 8, 9, 10]
list2 = ['f','u']
list3 = ['f','u']
# 增 append + extend
list.append(name)
print(list)
print(list+list2)
list.extend(list2)
print(list)

# 插入insert
list.insert(2,name)
print(list)

# 删除
# 删除一个
del list[2]
print(list)
# 删除列表
# del list3
# print(list3)#  NameError: name 'list3' is not defined

# 修改
# 修改一个
list[2] = name
print(list)
# 修改多个
list[2:5] = list2
print(list)
# 切片
list[4:4] = [-1,-2,-3]
print(list)

# pop 删除最后一个
list.pop()
print(list)
list.pop(3)
print(list)

# remove 删除指定值 第一个
list.remove('f')
print(list)

# clear 清空列表
list.clear()
print(list)

# in 判断是否包含
print('f' in list2)

# len 长度
print(len(list2))

# not in 判断是否不包含
print('f' not in list2)

# index 返回索引
print(list2.index('f'))

# count 计数
print(list2.count('f'))

# sort 排序
list2.sort()
print(list2)

# reverse 反转
list.reverse()
print(list)
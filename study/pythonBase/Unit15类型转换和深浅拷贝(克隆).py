#@Time : 2024/10/3 17:36
#@Auth : JMW

# TODO 类型转换
# 6大标准类型
# 1. Number数字: int整数 float浮点数 complex复数 bool布尔
# 2. String字符串 str()
# 3. List列表 list()
# 4. Tuple元组 tuple()
# 5. Dictionary字典 dict() 额外可能需要使用zip()函数进行压缩
# 6. Set集合 set()
# TODO Python中的很多基础类型的==运算符确实会调用对应对象的特殊方法__eq__()进行重写，以实现自定义的相等比较逻辑。

# 类型转换的特性 ：想要什么样类型，就用什么样函数


# TODO 什么是传递引用
# id(对象)方法可以查看内存地址
a = 10
b = 10
print(id(a))
print(id(b))
print(id(10))
print(a==b)
print(id(a)==id(b))
# 在Python中，相同的整数对象会被重用，以节省内存。所以`id(a)`、`id(b)`和`id(10)`的输出结果是一样的。
# 这段代码说明了传递引用的概念，即变量在赋值时实际上是引用了内存中的同一个对象。当多个变量引用同一个对象时，对其中一个变量的修改会影响到其他引用同一对象的变量。

print('——————————————————————————————————————')

str1 = "hello"
str2 = "hello"
print(id(str1))
print(id(str2))
print(id("hello"))
# Python中的很多基础类型的==运算符确实会调用对应对象的特殊方法__eq__()进行重写，以实现自定义的相等比较逻辑。
print(str1==str2)
print(id(str1)==id(str2))

print('——————————————————————————————————————')

list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))
print(id([1,2,3]))
print(list1==list2)
# Python中的很多基础类型的==运算符确实会调用对应对象的特殊方法__eq__()进行重写，以实现自定义的相等比较逻辑。
print(list1[1]==list2[1])
print(id(list1)==id(list2))
# 列表中，地址本身id是不相同的，而元素本身的id是相同的。

# TODO 拷贝 copy
import copy
a = [1,2,3]
a1 = copy.copy(a) # 复制a1信息
print(a)
print(a1)
print(id(a))
print(id(a1))
print(id(a[1]))
print(id(a1[1]))
# TODO 浅拷贝 新对象的子对象不拷贝 copy.copy(list1)
import copy

list1 = [1, 2, [3, 4]]
list2 = copy.copy(list1)

# 修改list1的子列表
list1[2][0] = 5

print(list1[2])  # 输出: [1, 2, [5, 4]]
print(list2[2])  # 输出: [1, 2, [5, 4]]
print(id(list1[2]))
print(id(list2[2]))
# TODO 深拷贝 新对象的子对象拷贝 copy.deepcopy(list1)
import copy

list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

# 修改list1的子列表
list1[2][0] = 5

print(list1[2])  # 输出: [1, 2, [5, 4]]
print(list2[2])  # 输出: [1, 2, [3, 4]]
print(id(list1[2]))
print(id(list2[2]))
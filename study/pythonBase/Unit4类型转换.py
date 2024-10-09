# 字符串
str = 'hello'
str2 = "hello"
print(str)
print(type(str2)) #查看字符串类型

# 三引号 ''' ''' 可以多行字符串
str3 = '''he
he
ha
'''
print(str3)

# 转义
str4 = 'hello\n\\world'
print(str4)

# 复制字符串 TODO 可以使用数值来对字符串复制。这算是和java不同的地方
str5 = 'hello' * 3
print(str5)

# in 语法 , not in 语法 TODO 判断字符串是否在另一个字符串中，类似java中的contains
print('h'in str5)
print('h' not in str5)

# r\R TODO 原样输出字符串内容
print(r'hello\nworld')

'''
格式化输出常用

格式化符号 | 转换
%d | 整数
%f | 浮点数
%s | 字符串
%x | 十六进制整数
%c | 单个字符
'''
name = 'fuck'
age = 178
print('%s,%d' % (name, age))
print('%s,%d' % ("name", 23))
# TODO {}写法
print('{}wcnmd{}'.format(12,23))
# TODO 带编号写法
print('{1}wcnmd{0}，{1}'.format(12,23))
# TODO 设置参数
print('{a}wcnmd{b}，{a}'.format(a=12,b=23))

# 运算符 TODO 多了一个取整除
a = 10
b = 3
print(a // b)
# 幂次方
print(a**b)


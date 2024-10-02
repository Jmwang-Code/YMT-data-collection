ans = '123456789787878787878787878'
# find
# 入参： 字符串.find(字串,起始位置,结束位置)
# 出参： 找到返回下标，找不到返回-1
print(ans.find('78',5,9))

# index
# 入参： 字符串.index(字串,起始位置,结束位置)
# 出参： 找到返回下标，找不到报错
print(ans.index('78',5,9))
import traceback
try:
    # 您的代码
    print(ans.index('890', 5, 9))
except ValueError as e:
    # 捕获 ValueError 异常并打印完整的错误消息和堆栈跟踪
    traceback.print_exc()

# count
# 入参： 字符串.count(字串,起始位置,结束位置)
# 出参： 找到返回个数，找不到返回0
print(ans.count('78',5,9))

# replace
# 入参： 字符串.replace(旧字串,新字串,替换次数)
# 出参： 返回替换后的字符串
print(ans.replace('78','90',1))

# split
# 入参： 字符串.split(分隔符,分隔次数)
# 出参： 返回列表
print(ans.split('78',1))

# capitalize
# 入参： 字符串.capitalize()
# 出参： 返回首字母大写的字符串
print(ans.capitalize())

# lower
# 入参： 字符串.lower()
# 出参： 返回小写字符串
print(ans.lower())

# upper
# 入参： 字符串.upper()
# 出参： 返回大写字符串
print(ans.upper())

# startswith
# 入参： 字符串.startswith(字串,起始位置,结束位置)
# 出参： 找到返回True，找不到返回False
print(ans.startswith('123',0,3))

# endswith
# 入参： 字符串.endswith(字串,起始位置,结束位置)
# 出参： 找到返回True，找不到返回False
print(ans.endswith('123',0,3))

# title
# 入参： 字符串.title()
# 出参： 返回首字母大写的字符串
print(ans.title())

# TODO 字符串判断
# islower
# 入参： 字符串.islower()
# 出参： 返回True，找不到返回False
print('是不是都小写',ans.islower())

# isupper
# 入参： 字符串.isupper()
# 出参： 返回True，找不到返回False
print('是不是都大写',ans.isupper())

# isspace
# 入参： 字符串.isspace()
# 出参： 返回True，找不到返回False
print('是不是都是空格',ans.isspace())

#isdigit
# 入参： 字符串.isdigit()
# 出参： 返回True，找不到返回False
print('是不是都是数字',ans.isdigit())

# TODO 字符串连接
# 1. +
print('+'+ans)
# 2. join
# 入参： 字符串.join(列表)
# 出参： 返回连接后的字符串
print(''.join(['1','2','3']))

# TODO 字符串删除
# 1. strip
# 入参： 字符串.strip(字符)
# 出参： 返回删除字符后的字符串
print(ans.strip('78'))

# 2. lstrip
# 入参： 字符串.lstrip(字符)
# 出参： 返回删除字符后的字符串
print(ans.lstrip('1'))

# 3. rstrip
# 入参： 字符串.rstrip(字符)
# 出参： 返回删除字符后的字符串
print(ans.rstrip('1'))


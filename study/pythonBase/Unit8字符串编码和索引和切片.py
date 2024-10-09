'''
 字符串编码
 万国码 unicode
 编码 UTF-8 对不同的字符用不同的长度
 编码 GBK 国标识别中文

 encode : 编码，字符转换成二进制字节流
 decode : 解码，二进制字节流转字符
'''

a = 'abcdefg'
a1 = a.encode()
print(a1)
a2 = a1.decode()
print(a2)

# TODO 索引  ,如果过界可能会出现 IndexError: string index out of range
print(a[3]) # 0 1 2 3
print(a[-3]) # -1 -2 -3

# TODO 切片 [启始索引:结束索引:步长]
print(a[0:3]) # [0,3) 0 1 2
'''
 步长有什么用呢？
 a = 'abcdefg'
print(a[::2])  # 输出结果为 "aceg"
在上面的代码中，[::2] 表示从字符串的第一个字符开始，每隔一个字符进行切片。因此，它会输出 'aceg'，即字符串 a 中每隔一个字符的子字符串。

a = 'abcdefg'
print(a[::-1])  # 输出结果为 "gfedcba"
在上面的代码中，[::-1] 表示从字符串的最后一个字符开始，每隔一个字符进行切片，并逆序输出。因此，它会将字符串反转并输出为 "gfedcba"。
'''



# 逻辑运算符 TODO python喜欢使用英文直接表达
True and False  # Java中： True&&False

True or False  # Java中： True||False

not True  # Java中： !True

# 三元表达式
a = 1
b = 2
c = 3
# 解释： 如果a>b则打印a，否则如果b>c则打印b，否则打印c
# python的三元表达式不如java 会分不清层次
print("a") if a > b else (print("b") if b > c else print("c"))
# TODO JAVA: 三元表达式 a>b?a:(b>c?b:c)  相对有层次感

# TEST
import random

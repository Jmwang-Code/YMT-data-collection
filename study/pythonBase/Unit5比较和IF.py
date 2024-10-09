# IF   TODO python的判断语法和java不同的地方
a = 1
if a>5:
    print("a")
elif a>2:
    print("b")
else:
    print("c")

# and or
score = int(input("请输入分数:"))
if score>5 and score<10:
    print("a")
elif score>2 or score<10:
    print("b")
else:
    print("c")

if score>5 and score<10:
    print("a")
# 这里通过控制缩进进行代码的执行范围
print("fuck")
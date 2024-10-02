# TODO 循环 while
from time import sleep

while True:
    print("Hello, World!")
    sleep(1)
    break

# for [0,10)
for i in range(10):
    print(i)

# [5,10) 整数
for i in range(5,10):
    print(i)

#TEST \t 水平制表符
for i in range(1,10):
    for j in range(1,i+1):(
        # f'的意义是 format
        # TODO java中System.out.print(i + "*" + j + "=" + (i * j) + "\t");，不会使用format
        print(f'{i}*{j}={i*j}' ,end='\t')
    )
    print()


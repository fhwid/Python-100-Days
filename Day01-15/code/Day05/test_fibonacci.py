"""
生成斐波那契数列的前20个数
"""

first = 1
second = 1
cnt = 2

while cnt <= 20:
    cnt += 1
    num = first + second
    print(num)

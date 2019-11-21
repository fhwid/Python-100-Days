"""
x1 + x2 + x3 + x4 = 8的所有正整数解
输入m和n计算C(m, n)
"""
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
#
# print(fm // fn // fmn)

def factorial(num):
    # 求阶乘
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

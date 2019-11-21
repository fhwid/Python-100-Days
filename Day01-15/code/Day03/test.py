"""
用户身份验证
"""

# username = input('请输入用户名：')
# password = input('请输入密码：')
# # 用户名是admin且密码是12345则身份验证通过，否则验证失败
# if username == 'admin' and password == '12345':
#     print('身份验证成功')
# else:
#     print('身份验证失败')

"""
分段函数求值
f(x) = 3x - 5   (x > 1)
     = x + 2    (-1 <= x <= 1)
     = 5x + x   (x < -1)
"""

# x = float(input('x = '))
# if x > 1 :
#     y = 3 * x - 5
# elif x >= -1 :
#     y = x + 2
# else :
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))
#

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number > answer:
#         print('大一点')
#     elif number < answer:
#         print('小一点')
#     else:
#         print('猜对了')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商明显不足！')

"""
输出九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end = '\t')
    print()

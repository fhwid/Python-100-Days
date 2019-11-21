import os
import time
import random
import string



def generate_code(code_len = 4):
    """
    生成指定长度的验证码
    :param code_len: 验证码长度（默认4个字符）
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename = '', has_dot = False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 返回文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x = []):
    """
    函数返回列表x中的最大和第二大的元素值
    :param x: 输入的列表
    :return: 返回x中的最大和第二大的值
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def is_leap_year(year):
    return 0 == year % 4 and 0 != year % 100 or 0 == year % 400

def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    # content = '北京欢迎你为你开天辟地...............'
    # while True:
    #     # 清理屏幕上的输出
    #     os.system('cls')
    #     print(content)
    #     # 休眠200 ms
    #     time.sleep(0.2)
    #     content = content[1:] + content[0]
    code = generate_code(8)
    xls_suff = get_suffix('test.xls', False)
    print(code)
    print(xls_suff)
    print(which_day(1980, 11, 28))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()


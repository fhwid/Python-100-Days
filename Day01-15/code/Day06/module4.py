# 求最大公约数
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 求最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

# 判断一个数是不是回文数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

# 判断一个数是不是素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_prime(num) and is_palindrome(num):
        print('%d是回文素数' % num)

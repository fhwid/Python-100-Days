"""
输出100以内的所有的素数
素数指的是只能被1和自身整除的正整数，不包括1
"""

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end = ' ')

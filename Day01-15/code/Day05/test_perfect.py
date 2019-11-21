"""
找出10000以内的完美数
"""

import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:# 排除num自身及factor重复的情况
                result += num // factor
    if result == num:
        print(num)
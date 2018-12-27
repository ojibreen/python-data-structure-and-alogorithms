'''
Author: ojibreen
Date: 12/23/2018
'''
import math


def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    base = max((10 ** int(math.ceil(len(str(num1)) / 2))), (10 ** int(math.ceil(len(str(num2)) / 2))))

    a = num1 // base
    b = num1 % base

    c = num2 // base
    d = num2 % base

    z2 = a * c
    z0 = b * d
    z1 = (a + b) * (c + d) - z2 - z0
    return (z2 * (base**2)) + (z1 * base) + z0

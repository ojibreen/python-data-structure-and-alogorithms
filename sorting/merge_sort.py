'''
Author: ojibreen
Date: 12/25/18
'''

import math


def sort(arr):
    if len(arr) == 1:
        return arr

    a, b = _split(arr)
    c = sort(a)
    d = sort(b)
    return _merge(c, d)


def _split(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arrs

    a = arr[0:math.floor(len(arr) / 2)]
    b = arr[math.floor(len(arr) / 2)::]
    return (a,b)


def _merge(a, b):
    merged = []
    i = 0
    j = 0
    a_done = False
    b_done = False
    for k in range(0, len(a) + len(b)):
        try:
            ai = a[i]
        except IndexError:
            ai = None

        try:
            bj = b[j]
        except IndexError:
            bj = None

        if ai != None and bj != None:
            if ai < bj:
                merged.append(ai)
                i += 1
            else:
                merged.append(bj)
                j += 1
        elif ai == None and bj != None:
            merged.append(bj)
            j += 1
        elif ai != None and bj == None:
            merged.append(ai)
            i += 1
    return merged
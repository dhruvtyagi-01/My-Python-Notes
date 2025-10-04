from functools import reduce

num = [68, 95, 43, 12, 50, 88, 26, 4, 30, 79, 71, 16, 92, 55, 61]

def maxNum(a, b):
    if a > b:
        return a
    return b

print(reduce(maxNum, num))
from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]


def square(n): return n * n


sqrList = map(square, l)
print(list(sqrList))

# Filter example

# def even(n):
#     if n % 2 == 0:
#         return True
#     return False


def even(n): return n % 2 == 0


onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example


def mySum(a, b): return a + b
def myMul(a, b): return a * b


add = reduce(mySum, l)
mul = reduce(myMul, l)

print(add)
print(mul)

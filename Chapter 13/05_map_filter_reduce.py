from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]

square = lambda n : n * n
sqrList = map(square, l)
print(list(sqrList))

# Filter example

                              # def even(n):
                              #     if n % 2 == 0:
                              #         return True
                              #     return False
even = lambda n: n % 2 == 0

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example

mySum = lambda a, b: a + b
myMul = lambda a, b: a * b

add = reduce(mySum, l)
mul = reduce(myMul, l)

print(add)
print(mul)
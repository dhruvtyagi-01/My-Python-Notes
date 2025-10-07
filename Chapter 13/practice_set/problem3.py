l = [68, 95, 43, 15, 50, 88, 26, 4, 30, 79, 70, 16, 92, 55, 61]


def div(n): return n % 5 == 0


newList = filter(div, l)

print(list(newList))

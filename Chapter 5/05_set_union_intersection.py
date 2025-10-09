s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

# print(s1.union(s2))
print(s1 | s2)

# print(s1.intersection(s2))
print(s1 & s2)

# print(s1.difference(s2))
print(s1 - s2)  # subtract set s2 from set s1

# print(s2.difference(s1))
print(s2 - s1)  # subtract set s1 from set s2

# print(s1.symmetric_difference(s2))
print(s1 ^ s2)

print(sorted(s1 | s2))

a = {20, 14, 12, 30}
print(set(sorted(a, reverse=True)))
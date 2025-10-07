dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
dict2 |= dict1

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
print(dict2)  # Output: {'b': 2, 'c': 4, 'a': 1}

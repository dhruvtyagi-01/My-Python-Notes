l = [22, 2, 4, 5, 7, 1]

# index = 1

# for item in l:
#     print(f"item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"item number at index {index} is {item}")

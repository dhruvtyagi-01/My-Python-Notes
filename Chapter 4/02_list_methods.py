friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends, "\n")

# append
friends.append("sweet")
print(friends, "\n")

num = [3, 7, 82, 901, 43, 821, 1, 63, 21]

# sort
num.sort()
print(num, "\n")

# reverse
num.reverse()
print(num, "\n")

# insert
num.insert(5, 92)  # insert 92 such that its index in the list is 5
print(num, "\n")

# pop
print(num.pop(4))
print(num, "\n")

# remove
num.remove(901)
print(num)

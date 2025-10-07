n = int(input("Enter number:"))
table = [str(n * i) for i in range(1, 11)]

l = "\n".join(table)
print(l)

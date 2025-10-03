n = int(input("Enter number:"))

table = [n * i for i in range(1, 11)]

print(table)

table = str(table)

with open("table.txt", "a") as f:   # "a" so it won’t overwrite
    f.write(f"\nTable of {n}: {table}")
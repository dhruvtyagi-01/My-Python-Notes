a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
c = int(input("Enter num 3:"))
d = int(input("Enter num 4:"))

if (a > b and a > c and a > d):
    print(a, "is greatest")

elif (b > c and b > d):
    print(b, "is greatest")

elif (c > d):
    print(c, "is greatest")

else:
    print(d, "is greatest")

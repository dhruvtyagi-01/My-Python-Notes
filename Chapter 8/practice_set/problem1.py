def greatest(a, b, c, d):
    if a > b and a > c and a > d:
        print(f"{a} is greatest")

    elif b > c and b > d:
        print(f"{b} is greatest")

    elif c > d:
        print(f"{c} is greatest")
    
    else:
        print(f"{d} is greatest")

a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))
d = int(input("Enter number:"))

greatest(a, b, c, d)
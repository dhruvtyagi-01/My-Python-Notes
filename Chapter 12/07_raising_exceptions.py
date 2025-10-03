a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

if b == 0:
    raise ZeroDivisionError("Division by 0 is not possible!")
else:
    print(f"Divsion of {a}/{b} is {a/b}")
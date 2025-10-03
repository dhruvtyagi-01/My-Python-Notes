try:
    a = int(input("Enter number 1:"))
    b = int(input("Enter number 2:"))

    print(f"Divsion of {a}/{b} is {a/b}")

except ZeroDivisionError as e:
    print("Infinite")
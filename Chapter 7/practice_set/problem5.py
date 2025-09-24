n = int(input("Enter number to find factorial:"))
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(factorial)
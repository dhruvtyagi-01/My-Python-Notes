n = int(input("Enter number:"))

if n == 0 or n == 1:
    print(f"{n} is not prime")

elif n < 0:
    print("Enter a positive number!")

else:
    for i in range(2, n):
        if (n % i == 0):
            print(f"{n} is not prime")
            break

    else:
        print(f"{n} is prime")

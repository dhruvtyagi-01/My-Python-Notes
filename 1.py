low = int(input("Enter lower range to find prime numbers: "))
up = int(input("Enter upper range to find prime numbers: "))
primeNums = []

for i in range(low, up + 1):

    if (i >= 2):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            primeNums.append(i)

print(primeNums)
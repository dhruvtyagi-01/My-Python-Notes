def recursive_sum(n):
    if(n == 0):
        return 0
    
    return n + recursive_sum(n - 1)

n = int(input("Enter number:"))

print(f"Sum is {recursive_sum(n)}")
num = int(input("Enter number to check palindrome: "))

temp = num
rev = 0

while temp != 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp //= 10
    
if rev == num:
    print("palindrome")
else:
    print("not palindrome")
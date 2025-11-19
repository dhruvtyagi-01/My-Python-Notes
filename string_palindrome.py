string = input("Enter string to check palindrome: ")
# rev = ""

# for item in string:
#     rev = item + rev
    
# if(rev == string):
#     print("palindrome")
# else:
#     print("not palindrome")

rev = string[-1::-1]

if rev == string:
    print("palindrome")
else:
    print("not palindrome")
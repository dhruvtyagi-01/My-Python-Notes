s1 = "Make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

text = input("Enter line:")

if(s1 in text or s2 in text or s3 in text or s4 in text):
    print("This comment is spam")

else:
    print("This comment is not spam")
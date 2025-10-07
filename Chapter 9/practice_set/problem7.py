with open("file(a).txt") as f:
    content_A = f.read()

with open("file(b).txt") as f:
    content_B = f.read()

if (content_A == content_B):
    print("Both files are identical and match content")
else:
    print("Files are not identical and do not match content")

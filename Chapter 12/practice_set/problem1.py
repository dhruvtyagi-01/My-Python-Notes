try:
    with(
        open('1.txt') as f1,
        open('2.txt') as f2,
        open('3.txt') as f3
    ):
        f1.read()
        f2.read()
        f3.read()

except Exception as e:
    print("There are no files as 1.txt, 2.txt, 3.txt")

print("Thank you")
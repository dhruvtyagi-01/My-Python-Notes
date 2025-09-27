with open("09_problem1_poem.txt") as f:
    text = f.read().lower()

word = input("Enter the word you want to check:").lower()

if(word in text):
    print(f"It contains \"{word}\"")

else:
    print(f"It doesn't contains {word}")
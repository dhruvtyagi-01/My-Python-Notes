with open("log.txt") as f:
    words = f.read().lower()

word = "python"

if(word in words):
    print(f"Log contains word {word}")
    print(words.count(word))
else:
    print(f"Log doesn't contains word {word}")
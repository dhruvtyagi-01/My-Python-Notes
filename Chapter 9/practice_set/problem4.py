with open("file(4).txt") as f:
    words = f.read().lower()

censor_words = ["donkey", "it", "the", "as"]

censored_text = words

for word in words:
    censored_text = censored_text.replace(word, "####")

with open("file(4).txt", "w") as f:
    f.write(censored_text)
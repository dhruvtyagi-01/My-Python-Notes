with open("log.txt") as f:
    lines = f.readlines()

lineNo = 1
word = "python"

for line in lines:
    if word in line.lower():
        print(f"Log contains word '{word}' in line no. {lineNo}")
    else:
        print(f"Log doesn't contain word '{word}' in line no. {lineNo}")
    lineNo += 1

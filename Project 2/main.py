import random

randomNum = random.randint(1, 100)
guess = 0

print("\t\t--> GAME STARTED <--")

while(True):
    target = int(input("Enter your guess:"))

    if target < 1 or target > 100:
        print("Guess within range of 1-100")
        continue

    guess += 1

    if target < randomNum:
        print("Higher number please")
    
    elif target > randomNum:
        print("Lower number please")
    
    else:
        print("You won!")
        break
    
print(f"It took you {guess} guesses")
import random


def game():
    print("You are playing the game")
    score = random.randint(1, 50)

# Fetch the highscore
    with open("highscore.txt") as f:
        highscore = f.read()

        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score is {score}")

    if (score > highscore):
        # Write this highscore to file
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score


game()

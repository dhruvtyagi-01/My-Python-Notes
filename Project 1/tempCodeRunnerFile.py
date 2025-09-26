import random

'''
1 = snake
-1 = water
0 = gun
'''

round = int(input("No. of rounds you want to play:"))
print("\t\t--> GAME STARTED <--")

for i in range(0, round):
    numbers = [-1, 0, 1]
    computer = random.choice(numbers)

    print("s for Snake, w for Water , g for Gun")
    youStr = input("Your Choice:")

    youDict = {
        "s" : 1,
        "w" : -1,
        "g" : 0
    }
    you = youDict[youStr]

    reverseDict = {
        1: "Snake",
        -1: "Water",
        0: "Gun",
    }

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if (computer == you):
        print("Tie")

    else:
        if (computer == 1 and you == -1):
            print("You Lose")

        elif (computer == 1 and you == 0):
            print("You Win!")

        elif (computer == -1 and you == 1):
            print("You Win!")

        elif (computer == -1 and you == 0):
            print("You Lose")

        elif (computer == 0 and you == 1):
            print("You Lose")

        elif (computer == 0 and you == -1):
            print("You Win!")

    con_tinue = input("Do you want to continue? (y or n):\n")

    if(con_tinue == "y"):
        continue

    elif(con_tinue == "n"):
        break

print("THANK YOU FOR PLAYING!")
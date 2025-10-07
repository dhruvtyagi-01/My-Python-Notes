state = ""

while (True):
    inp = input(">")
    if (inp.lower() == 'help'):
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif inp.lower() == 'start':
        if (state == "start"):
            print("car is already moving!")
        else:
            print("The car has started , READY TO GO :)")
            state = inp
    elif inp.lower() == 'stop':
        if state == "stop":
            print("Car is already stopped!")
        else:
            print("You stopped the car :(")
            state = inp
    elif inp.lower() == 'quit':
        print("Game ended!!")
        break
    else:
        print("Invalid input")

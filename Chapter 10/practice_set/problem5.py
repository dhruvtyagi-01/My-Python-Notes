from random import randint  # use of "from" keyword
# import random


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(
            f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no:{self.trainNo} is running")

    def getFare(self, fro, to):
        print(
            f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(10, 2000)}")


train = Train(54236)

train.bookTicket("Old Delhi", "Mumbai")
train.getStatus()
train.getFare("Old Delhi", "Mumbai")

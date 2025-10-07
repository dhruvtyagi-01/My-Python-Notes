class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


m = Number(1)
n = Number(2)

print(m + n)

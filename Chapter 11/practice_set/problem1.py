class TWODvector:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class THREEDvector(TWODvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TWODvector(3, 6)
a.show()

b = THREEDvector(5, 8, 9)
b.show()

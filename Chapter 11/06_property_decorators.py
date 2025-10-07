class Demo:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Demo()
e.name = "Dhruv Tyagi"
print(e.name)

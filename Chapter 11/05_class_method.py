class Demo:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")


e = Demo()
e.a = 5

e.show()

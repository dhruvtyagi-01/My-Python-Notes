class Calculator:

    @staticmethod
    def greet():
        print("Hello!")

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square is {pow(self.n, 2)}")

    def cube(self):
        print(f"Cube is {pow(self.n, 3)}")

    def square_root(self):
        print(f"Square root is {pow(self.n, 1/2)}")

Calculator.greet()

value = float(input("Enter value to calculate:"))
a = Calculator(value)
a.square()
a.cube()
a.square_root()
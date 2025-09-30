class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello!")

dhruv = Employee()
dhruv.language = "C" # This is an instance attribute

dhruv.greet()
dhruv.getInfo()
# Employee.getInfo(dhruv)
class Employee:
    language = "Py"
    salary = 1200000

    def __init__(self, name, salary, language):  # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I created an object")


dhruv = Employee("Dhruv", 1200000, "C")

# dhruv.name = "Dhruv"
print(dhruv.name, dhruv.salary, dhruv.language)

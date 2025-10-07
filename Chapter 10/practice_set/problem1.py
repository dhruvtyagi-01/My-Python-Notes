class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


p = Programmer("Dhruv", 1200000)
print(p.name, p.salary, p.company)

r = Programmer("Rohan", 1200000,)
print(r.name, r.salary, r.company)

class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


dhruv = Employee()
dhruv.language = "C" # This is an instance attribute
print(dhruv.language, dhruv.salary)
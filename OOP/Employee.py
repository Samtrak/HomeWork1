class Employee:
    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def __str__(self):
        return "Employee[" + \
               "id=" + str(self.id) + "," + \
               "name=" + self.firstName + " lastname=" + self.lastName + "," + \
               "salary=" + str(self.salary) + \
               "]"

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getSalary(self):
        return self.salary

    def getName(self):
        return self.firstName + " " + self.lastName

    def setSalary(self, newSalary):
        self.salary = newSalary

    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self, percent):
        self.salary = self.salary + self.salary * (percent / 100.0)


# ===================== Running classes ===============

Timur = Employee(1, "Timur", "Ivanov", 200)
print(Timur)

print(Timur.getID())
print(Timur.getFirstName())
print(Timur.getLastName())
print(Timur.getSalary())
print(Timur.getName())

Timur.setSalary(100.0)
print(Timur.getAnnualSalary())

Timur.raiseSalary(5)

print(Timur)


























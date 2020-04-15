class Account:
    def __init__(self, id ,name, balance = 0):
        self.id = id
        self.name = name
        self.balance = balance
    def __str__(self):
        return "Account [" + "id=" + str(self.id)+","+"name="+self.name + "," +"balance="+ str(self.balance)+"]"
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance
    def getAmount(self):
        return self.getBalance()
    def setID(self, newId):
        self.id = newId
    def setName(self, newName):
        self.name = newName
    def setBalance(self, newBalance):
        self.balance = newBalance

a= Account("5","Hasan")
b = Account("7","Bek",6)
print(a.getID())
print(a.getName())
print(b.getID())
print(b.getName())
print(b.getBalance())

Asan = Account(5, "Asan", 0)
print(Asan.getID())
print(Asan.getName())
print(Asan.getBalance())
print(Asan)

    
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

    def credit(self, amount):
        if amount >= 0:
            self.balance += amount

            return self.balance

    def debit(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else:
            print("amount exceeded")

        return self.balance

    def transferTo(self, another, amount):
        if self.balance >= amount:
            self.balance -= amount
            another.credit(amount)
        else:
            print("amount exceeded")

        return self.balance

a= Account("5","Hasan")
b = Account("7","Bek",2000)
print(a.credit(700))
print(a.debit(400))
print(a.transferTo(b, 100))
Asan = Account(5, "Asan", 0)
print(Asan)

    
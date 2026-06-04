class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("owner:",self.owner)
        print("New Balance:", self.balance)
acc1 = BankAccount("Anjina",2000)
acc1.deposit(500)
acc1.deposit(300)
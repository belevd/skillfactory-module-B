class Client:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def changeBalance(self, balance):
        self.balance = balance
        return f'Новый баланс равен {self.balance}'

    def charge(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f'Произошла расходная операция в размере {amount}. Текущий баланс равен {self.balance}'
        else:
            return f'Данная операция не может быть произведена. На счету недостаточно средств.\nТекущий баланс равен {self.balance}'

    def fill(self, amount):
        self.balance += amount
        return f'Произведена операция пополнения счета на сумму {amount}. Текущий баланс равен {self.balance}'

    def clientInfo(self):
        return f'Клиент «{self.name}». Баланс: {self.balance} руб.'

client_1 = Client('Иван Петров', 50)
client_1.charge(15)
client_1.fill(40)
print(client_1.clientInfo())
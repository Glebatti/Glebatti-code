# Магические методы
# __add__, __mul__, __sub__, __truediv__

class BankAccount:
    def __init__(self,name, balance):
        print("new_obj init")
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    def __add__(self, other):           #сложение двух параметров (баланса)
        print("__add__ call")
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int,float)):
            return BankAccount(self.name, self.balance+other)
        raise NotImplemented

    def __mul__(self, other):           #умножение двух параметров (баланса)
        print("__add__ mul")
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int,float)):
            return self.balance * other
        if isinstance(other,str):
            return self.name + other
        raise NotImplemented

    def __radd__(self, other):
        print("__radd__ call")
        return self + other

b = BankAccount("ivan", 920)
r = BankAccount("Misha",78)
print(r+900.6)
print(r+b)
print(2+b)
print(b*3)
print(b*"ttt")
m = BankAccount("Tom", 200)
d = m+50
print(d)
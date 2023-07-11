# Магические методы __str__ и __repr__

class Lion:
    def __init__(self, name):
        self.name = name

# q = Lion ("Bob")
# print(q)
    def __repr__(self): #метод отображает правильное имя класса(можно добавить дополнительные символы) а не контрольную сумму в принте
        return f"The object Lion - {self.name}"
    def __str__(self): #метод отображает правильное имя класса а не контрольную сумму в принте
        return f"Lion - {self.name}"
s = Lion("Simba")
w = Lion("Vasya")
print(s)
print(w)
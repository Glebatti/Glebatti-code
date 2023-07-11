# Наследование Введение

class Person: #parent

    def can_breathe(self):
        print("Я могу дышать")

    def can_walk(self):
        print("Я могу ходить")

class Doctor(Person): #subclass

    def can_cure(self):
        print("Я могу лечить")

class Ortoped(Doctor):
    pass

class Architect(Person): #subclass

    def can_build(self):
        print("Я могу построить здание")

d = Doctor()
a = Architect()
e = Ortoped()
d.can_cure()
d.can_walk()
d.can_breathe()
a.can_build()
a.can_walk()
d.can_breathe()
print(issubclass(Doctor, Person)) #проверка класса родителя и потомка
print(issubclass(Person, Doctor)) #проверка класса родителя и потомка
print(isinstance(d,Doctor))
print(isinstance(d,Person))
print(isinstance(a,Person))
e.can_breathe()
e.can_cure()
e.can_walk()
class Car:
    model = "BMW"
    engine = 1.6
    @staticmethod    # декоратор,который позволяет вызывать функцию drive из экземплра класса
    def drive():
        print("Lets go")

a1 = Car() #экземпляры класса
a2 = Car() #экземпляры класса
print(a1.model, a2.engine)
a1.seat = 4
a1.model = "Lada" #атрибут создатся только в экземпляре класса
print(a1.__dict__)
a2.size = 80 #атрибут создатся только в экземпляре класса

print(a2.size)
Car.r = 100 #к атрибуту можно обратиться из всех эеземпляров класса

print(a1.r, a2.r)

print(a1.seat)

del a1.model #удаление атрибута будет только в экземпляре класса ,но при обращении к этому атрибуту значение присвоется из основного класса

# print(a1.model)

print(Car.drive()) #скобочки это вызов функции

b = Car()

print(b.drive())
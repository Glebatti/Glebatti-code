class Car:
    model = "BMW"
    engine = 1.6

a = Car()
print(type(a))
print(isinstance(a, Car))

class Person:
    name = "Ivan"     #атрибуты класса
    age = 30

print(Person.name,Person.age)

m = Person.__dict__   #посмотреть все атрибуты класса
print(m)

print(getattr(Person, "name")) #обратиться к атрибуту класса

print(getattr(Person,"x",100)) # вернет 100 если не найдет атрибут x

Person.name = "Misha"
Person.x = 200


setattr(Person, "y",500) #установть значение атрибута и создать его


del Person.x #удалить атрибуты
# print(m)

delattr(Person,"y") #удалить атрибуты
# print(m)

a = Person()
b = Person()

Person.z = 100

del Person.age
Person.name = "Nen"
print(Person.__dict__, Person.__dict__)
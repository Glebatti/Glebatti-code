class Cat:


    def set_value(self, value, age=0):
        self.name = name
        self.age = age

    def __init__(self, name, breed="pers", age=1, color="white"):
        print("Hello new object is ", self, name, breed, age, color)
        self.name = name  #методы класса
        self.age = age
        self.breed = breed
        self.color = color
# bob = Cat()
# bob.set_value("Bob")
tom = Cat("Tom", "siam", 40, "black")
print(tom)

walt = Cat("Walt")
kelly = Cat("kelly", age=88) #передача входящих аргументов(параметров) методам класса(именам атрибутов)
print(walt)
print(Kelly)



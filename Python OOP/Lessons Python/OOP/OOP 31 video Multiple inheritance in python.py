# Множественное наследование

class Doctor:
    def __init__(self, degree):
        self.degree = degree
    def graduate(self):
        print("Ура , я отучился на доктора")
    def can_build(self):
        print("Я доктор,я тоже умею строить,но не очень")

class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print("Ура , я отучился на строителя")
    def can_build(self):
        print("Я строитель,я умею строить")

class Person(Builder,Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)
    def __str__(self):
        return f" Person {self.rank} {self.degree}"

    def graduate(self):
        print("Посмотрим кем я стал")
        super().graduate()
        Doctor.graduate(self)


print(Person.__mro__)
s = Person(5, "spec")
#s.can_build()
#s.can_cure()
# s.graduate()
print(s)
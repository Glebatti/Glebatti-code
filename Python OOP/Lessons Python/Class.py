class House():
    "описание дома"
    def __init__(self,street,number):
        "свойство дома"
        self.street = street
        self.number = number
        self.age = 8

    def build(self):
        "строить дом"
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")
    def age_of_house(self, year):
        "возраст дома"
        self.age += year


# House1 = House("Московская",20)
# House2 = House("Московская",21)
#
# House1.build()
# House1.age_of_house(5)
# print(House1.age)

class ProspectHouse(House):
    "дома на проспекте"
    def __init__(self,prospect, number):
        super().__init__(self,number)
        self.prospect = prospect

PrHouse = ProspectHouse("Ленина", 5 )
print(PrHouse.prospect,PrHouse.number)

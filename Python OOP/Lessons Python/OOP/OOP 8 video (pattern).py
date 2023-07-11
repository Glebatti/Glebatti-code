class Cat:
    __shared_attr = {"breed": 'pers', "color": 'black'}

    def __init__(self):
        self.__dict__ = Cat.__shared_attr

d = Cat()
g = Cat()
d.breed = "siam"
d.name = "Bob"
h = Cat()
print(h.__dict__)
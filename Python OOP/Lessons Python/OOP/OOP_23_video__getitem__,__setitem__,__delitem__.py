# Магические методы __getitem__,__setitem__,__delitem__

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):  # взять индекс массива
        if 1 <= item <= len(self.values):  #сделали начало счета индекса с 1
            return self.values[item - 1]
        else:
            raise IndexError("Индекс за границей диапазона массива")

    def __setitem__(self, key, value):  # поменять индекс массива
        if 1 <= key < len(self.values): #сделали начало счета индекса с 1
            self.values[key - 1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]*diff)
            self.values[key - 1] = value
        else:
            raise IndexError("Индекс за границей диапазона массива")

    def __delitem__(self, key):  # удалить индекс массива
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError("Индекс за границей диапазона массива")


v1 = Vector(1, 2, 434, 32)
print(v1)
print(v1[2])
print(v1[1])
v5 = Vector(4, 6, 7, 7, 5, 4)
v5[2] = 100
del v5[4]
print(v5)

v7 = Vector(55,46,33,662,264,75574,4)
print(v7[1])

v10 = Vector(1,2,2)
v10[10] = 200
print(v10)

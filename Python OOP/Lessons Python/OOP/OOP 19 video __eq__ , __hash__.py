#Магические методы __eq__ and __hash__  сравнение

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))


# p1 = Point()
# isinstance(p1, object)

p3 = Point(1,2)
p4 = Point(1,2)

print(p3 == p4)

p6 = Point(3,4)
p7 = Point(30,40)

print(hash(p3))
print(hash(p4))
r = {}
r[p6] = 100
print(r)

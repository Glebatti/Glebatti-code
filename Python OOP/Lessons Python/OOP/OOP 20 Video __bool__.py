class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("call __len__")
        return abs(self.x - self.y)

    def __bool__(self):                   #возвращает true или false в сзависимости от заданнызх параметров класса
        print("call __bool__")
        return self.x != 0 or self.y != 0


p1 = Point(1, 2)
print(bool(p1))

p2 = Point(9, 9)
p3 = Point(0, 0)
print(bool(p2))
print(bool(Point(0,-7)))
print(bool(Point(0,0)))

if p1:
    print("hello")

if p3:
    print("hay")
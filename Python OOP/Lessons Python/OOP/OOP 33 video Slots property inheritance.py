# Slots,property и наследование

class Rectangle:
    __slots__ = "__width", "height"

    def __init__(self, a, b):
        self.width = a
        self.height = b
    @property
    def width(self):
        # return (self.height+self.width)*2
        return self.__width
    @width.setter
    def width(self, value):
        print("setter called")
        #return (self.height * self.width)
        self.__width = value

class Square(Rectangle):
    __slots__ = tuple()
    def __init__(self,a, b):
        super().__init__(a,b)

a = Rectangle(3,4)
#print(a.area,a.perimetr)
print(a.width)
print(a._Rectangle__width)
# s = Square(4,5)
# print(s.__dict__)
# s.zz = 100
d = Square(4,4)
print(d.width,d.height)




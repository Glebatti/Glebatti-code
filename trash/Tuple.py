# marx_tuple = ("Groucho","Chico","Harpo")
# a, b, c = marx_tuple
# print(a)
def sayHello():
    print("Привет Мир")
sayHello()
def printMax(a,b):
    if a>b:
        print(a,"максимально")
    elif a==b:
        print(a,"равно",
    else:
        print(b,"максимально")
printMax(3,3)
x=5
y=7
printMax(x,y)

x=50
def func(x):
    print("x равен",x)
    x=2
    print("замена локального х на",x)
func(x)
print("x по прежнему",x)


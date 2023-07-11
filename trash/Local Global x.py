def sayHello():
    print("Привет Мир")
sayHello()
def printMax(a,b):
    if a>b:
        print(a,"максимально")
    elif a==b:
        print(a,"равно",b)
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

x=50
def func():
    global x
    print("x равен", x)
    x = 2
    print("заменяем глобальное значение х на", x)
func()
print("Значение x составляет",x)

def func_outer():
    x=2
    print("x равно",x)

    def func_inner():
        nonlocal x
        x=5
    func_inner()
    print("Локальное x сменилось на",x)
func_outer()

def say(message,times=1):
    print(message*times)
say("Привет")
say("Мир",6)

def func(a,b=5,c=10):
    print("a равно",a, "b равно",b, "c равно",c)
func(3,7)
func(25,c=24)
func(c=50,a=100)
func(b=500,a=1)

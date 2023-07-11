def hello():
    print("Привет мир")
hello()
hello()

x = int(input("Введите 1 число: "))
y = int(input("Введите 2 число: "))

def sum(a,b):
    return a+b
print(sum(x,y))

def f(a=2):
    return 2*a-2
print(f(4))

b = 45
def f():
    global b
    b = b + 2
    print(b)
f()
print(b)

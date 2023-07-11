def summa(*args):
    print(args)  #выводит кортеж из аргументов
summa(7,8,9,1,10)

def brand(**kwargs):
    for x, y in kwargs.items(): # выводит словарь с ключами
        print(x, ':',y)

brand(a = "Apple",s="Samsung")
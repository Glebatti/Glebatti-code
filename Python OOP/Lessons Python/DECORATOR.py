def header(func):

    def inner(*args,**kwargs):  #произвольное колво аргуметов(позиционных и именованных)
        print("<h1>")
        func(*args,**kwargs)
        print("</h1>")
    return inner

def table(func):

    def inner(*args,**kwargs):  #произвольное колво аргуметов(позиционных и именованных)
        print("<table>")
        func(*args,**kwargs)
        print("</table>")
    return inner

@header #say = header(say)
@table #say = header(table(say))
def say(name,surname,age):
    print("hello",name,surname,age)

def buy():
    print("buy world")

#say = header(table(say)) # вызов 2 декараторов
say("Vasya","Ivanov",30)
header(buy)
buy()

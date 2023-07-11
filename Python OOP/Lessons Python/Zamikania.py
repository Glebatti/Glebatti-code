import builtins
print(dir(builtins))


def degree(x):
    y = 2
    def degree_two():
        return y ** x
    return degree_two()
print(degree(4))

def message(number):
    def print_message():
        return "Число " + str(number)
    return print_message()
print(message(78))

def message1(x):
    def print_message1(y):
        return x, y
    return print_message1
d = message1(4)
print(d(5))
print(d(8))
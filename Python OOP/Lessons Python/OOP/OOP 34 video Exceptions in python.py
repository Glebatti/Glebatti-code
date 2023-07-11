# Исключения в питоне
print("Hello1")
print("Hello2")
print("Hello3")
try:
    {}[5]
    # int("Hello")
except KeyError:
    print("Неправильное преобразование")

try:
   a = int(input(66))
except:
    raise ValueError("Неправильное значение")
print("Hello4")
print("Hello5")
print("Hello6")
t = IndexError()
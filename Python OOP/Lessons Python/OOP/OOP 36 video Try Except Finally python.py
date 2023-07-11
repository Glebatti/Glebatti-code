# Обработка исключений
s = "hello"
d = {}
# f = open("11.txt")
try:
    # 1 / 0
    # int("hello")
    # a+b
    # d["key"]
    # s[6]
    # 4+"fds"
    # execute(f)
    1
except ValueError:
    print("error ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("error NameError")
except LookupError:
    print("error LookupError")
except Exception:
    print("error")
else:
    print("good")
finally:
    print("end")
    # f.close()
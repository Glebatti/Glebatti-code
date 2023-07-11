# инструкция raise

# er = Exception("Big error",1,2)
# raise er

try:
    # 1/0
    # {}["k"]
    [1,2,3][15]
except (KeyError, IndexError) as error:
    # print("LookupError")
    print(f"Logging error: {error} {repr(error)}")
    raise TypeError('ошибка типа') from None
except ZeroDivisionError as err:
    print("ZeroDivisionError")
    print(f"Logging error: {err} {repr(err)}")

try:
    raise ValueError('ошибка типа')
except ValueError as first:
    try:
        raise ("ошибка типа")
    except TypeError as second:
        raise Exception("Большое исключение") from first


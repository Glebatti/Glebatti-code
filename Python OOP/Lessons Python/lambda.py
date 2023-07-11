def rectangle_area(a,b):
    return  a * b
print(rectangle_area(4,7))


print((lambda a, b: a * b)(17,14))

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(maximum(5, 17))

print((lambda a,b: a if a > b else b)(25,14))
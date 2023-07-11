# with open("33.txt") as f:
#     n = int(f.readline())
#     for i in range(n):
#         if i != "\n":
#             a,b = map(int,f.readline().split())
#             print(a,b)
#         else:
#             continue

def f(a,b):
    return a*b
a = map(f, [2,4,5],[5,6])
print(list(a))

m = map(lambda x: x+15, (2,4,5))
print(list(m))

def u(o):
    if o % 2 ==0:
        return o
o = filter(u,(2,4,5))
print(list(o))

LL= filter(lambda x: (x % 2==0),(2,4,5))
print(list(LL))

from functools import reduce
print(reduce(lambda a,b: a * b,(50,57,89,12,100)))

a = [1,2,3,4,5,6]
b = "abcdef"
result = zip(a,b)
print(list(result))
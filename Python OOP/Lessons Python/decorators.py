from _datetime import datetime

# Декораторы

def timeit(func):
    def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
    return wrapper()


@timeit
def one(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 ==0:
           l.append(i)
    # print(datetime.now() - start)
    return l


@timeit
def two(n):
    # start = datetime.now()
    l =[x for x in range(10**4) if x % 2 ==0]
    # print(datetime.now()-start)
    return l


l1 = one
a = l1(10)
print(a)
# print(l1,l2)

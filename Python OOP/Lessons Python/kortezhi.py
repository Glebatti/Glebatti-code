tupl = ("first",)
print(type(tuple))

array = list(tupl)
print(array)
A = [1,2,4]
print(tuple(A))

dict = {"яблоко": "красное", "банан":"желтый", "лимон":"желтый"}
for k in dict.items():
    print(k)
for j in dict.keys():
    print(j)
for m in dict.values():
    print(m)
print(dict["банан"])
dict["банан"] = "зеленый"
print(dict)
del dict["яблоко"]
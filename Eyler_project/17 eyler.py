from num2words import num2words
A = []
Result = ""
for j in range(1, 1001):
    m = num2words(j)
    # print(m)
    Result += m
#     A.append(m)
# Result = ("".join(map(str, A)))
Konec = Result.replace("-", "")
Konec = Konec.replace(" ","")
# print(Konec)
print(len(Konec))
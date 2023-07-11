s = open("C:\Work Python\Eyler\Python Fule 8 Eyler.txt", "r")
m=s.read()
A=list(m)
res = [int(elem) for elem in A if elem.isdigit()]
#print(res)
maxi=1
m=0
for j in range(1001-13):
    multi = 1
    spisok = (res[j: (j + 13)])
    for chislo in spisok:
        multi *= chislo
    if maxi < multi:
       maxi = multi
print(maxi)
# m=str(m)
# H=list(m[0:10])
# Result=[int(elem) for elem in H if elem.isdigit()]
# OOO = int(''.join(map(str, Result)))
# print(OOO)
#     maxi=maxi+i
# print(maxi)multi=multi+i
#         if maxi<multi:
#             maxi=multi
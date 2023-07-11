s = open("C:\Work Python\Python File 13 Eyler.txt", "r")
m=s.read()
A=list(m)
res = [int(elem) for elem in A if elem.isdigit()]
#print(res)
maxi=1
m=0
for j in range(0,5000,50):
    #for i in ((res[j : (j + 50)])):
        # print(res[j : (j + 50)])
    n = int(''.join(map(str, res[j : (j + 50)])))
    m=m+n
m=str(m)
H=list(m[0:10])
Result=[int(elem) for elem in H if elem.isdigit()]
OOO = int(''.join(map(str, Result)))
print(OOO)
#     maxi=maxi+i
# print(maxi)multi=multi+i
#         if maxi<multi:
#             maxi=multi
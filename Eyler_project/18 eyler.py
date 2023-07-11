with open("18 eyler file.txt","r") as conf:
     a = conf.read()
     spisok = list(a)
chislo = ""
array = []
res = []
maxi_put = 0
for elem in spisok:
     if elem == " ":
          continue
     if elem == "\n":
           array.append(res)
           res = []
           continue
     chislo += elem
     if len(chislo) == 2:
        n = int(chislo)
        res.append(n)
        chislo = ""
#print(res)
pos = 0
count =0
# for j in range(0, len(array)):
#     row = array[j]
#     srez = row
#     if len(row) > 2:
#         # pos = array2.index(max(array2))+1
#         srez = row[pos:pos+2]
#         count+=1
#     maximum = max(srez)
#     pos = row.index(max(srez))
#     maxi_put += maximum
# print(maxi_put)
count = 0
while len(array) > 1:
#for j in range(len(array)-1, 0, -1):
    row = array.pop(-1)
    for m in range(len(array[-1])):
        array[-1][m] = max([array[-1][m]+row[m], array[-1][m]+row[m+1]])
        print(array[-1])
maxpath = array[0][0]

print(maxpath)





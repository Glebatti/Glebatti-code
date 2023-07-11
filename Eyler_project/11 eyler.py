s = open("C:\Work Python\Eyler\Python file 11 eyler.txt", "r")
file = s.read()
# res = [int(elem) for elem in file if elem.isdigit()]
# A=list(m)
res = []
chislo = ""
Array = []
diagonalP = []
diagonalL = []
vertical = []
maxi = 1
maxi1 = 1
maxi2 = 1
maxi3 = 1
i4 = 0
for elem in file:
    if elem == " ":
        continue
    if elem =="\n":
        Array.append(res)
        res = []
        continue
    chislo += elem
    if len(chislo) == 2:
        n = int(chislo)
        res.append(n)
        chislo = ""
for i in range(len(Array)):       #// горизонталь и вертикаль
    for i2 in range(len(Array[i])):
        goris = (Array[i][i2:i2+4])
        multi = 1
        y = (Array[i2][i])
        vertical.append(y)
        if len(goris)==4:
            for elem_gor in goris:
                multi *= elem_gor
                if maxi < multi:
                   maxi = multi
        else:
            continue
        # print(goris) #// сумма горизонтали

for j in range(len(vertical)):
    spisok = (vertical[j: (j + 4)])
    multi1 = 1
    for elem_vert in spisok:
        multi1 *= elem_vert
        if maxi1 < multi1:
           maxi1 = multi1
        if len(spisok) < 4:
           break


# diagonals = [[] for i in range(N + M - 1)]
# for i in range(-(N - 1), M):
for i4 in range(17):
    for i3 in range(3,-1,-1):       #// диагонали
        diagonalP.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(7, 3, -1):  # // диагонали
        diagonalP.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(11, 7, -1):  # // диагонали
        diagonalP.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(15, 11, -1):  # // диагонали
        diagonalP.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(19, 15, -1):  # // диагонали
        diagonalP.append(Array[i3][i4])
        i4 += 1

for j in range(len(diagonalP)):
    spisok_P = (diagonalP[j: (j + 4)])
    multi2 = 1
    for elem_vert in spisok_P:
        multi2 *= elem_vert
        if maxi2 < multi2:
           maxi2 = multi2
        if len(spisok_P) < 4:
           break

for i4 in range(17):
    for i3 in range(0,4):       #// диагонали
        diagonalL.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(4,8):  # // диагонали
        diagonalL.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(8,12):  # // диагонали
        diagonalL.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(12,16):  # // диагонали
        diagonalL.append(Array[i3][i4])
        i4 += 1
for i4 in range(17):
    for i3 in range(16,20):  # // диагонали
        diagonalL.append(Array[i3][i4])
        i4 += 1

for j in range(len(diagonalL)):
    spisok_L = (diagonalL[j: (j + 4)])
    multi3 = 1
    for elem_vert in spisok_L:
        multi3 *= elem_vert
        if maxi3 < multi3:
           maxi3 = multi3
        if len(spisok_L) < 4:
           break

print(maxi)
print(maxi1)
print(maxi2)
print(maxi3)
print(diagonalP)



# for b in range(20):
#     for i in range(len(Array)):
#         z = (Array[i][i+b])
#         diagonalP.append(z)
# print(diagonalP)
        # d = (Array[i2][19-i2])
            # diagonalL.append(d)
            #
            #
#         spisok = (Array[2:,3:])
#         break
# print(spisok)
# #     for chislo in spisok:
# #         multi *= chislo
# #     if maxi < multi:
# #        maxi = multi
# # print(maxi)




# print(Array)
# for row in Array:            # делаем перебор всех строк матрицы A
#      for e in row:     # перебираем все элементы в строке row
#          print(e, end =' ')
#          # if len(str(e))==1:
#          #    print(sep = " ")
#      print()
# #

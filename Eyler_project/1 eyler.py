# r=0
# for i in range(1,1000):
#     if i % 3 ==0 or i % 5==0:
#         r=r+i
# print(r)

count = 0
A = []
Stop = True
i=0
while Stop == True:
    i += 1
    Delitel = []
    A.append(i)
    # print(A)
    Summa = sum(A)
    # print(Summa)
    for j in range(1, Summa+1):
        if Summa % j == 0:
            Delitel.append(j)
            if len(Delitel) == 201:
                Stop = False
                print(Summa, Delitel, sep=" делители" )
                print(len(Delitel))
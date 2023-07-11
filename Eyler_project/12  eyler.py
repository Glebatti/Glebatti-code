
A = []
Stop = True
i = 0
while Stop == True:
    count = 0
    i += 1
    Delitel = []
    A.append(i)
    # print(A)
    Summa = sum(A)
    # print(Summa)
    for j in range(1, Summa+1):
        if Summa % j == 0:
            Delitel.append(j)
            Para = Summa / j
            Delitel.append(Para)
            if j >= Para:
                Delitel.pop(len(Delitel)-1)
                Delitel.pop(len(Delitel) - 2)
                break
            if len(Delitel) > 500:
                Stop = False
    print(Summa)
print(Summa, Delitel, sep=" делители")



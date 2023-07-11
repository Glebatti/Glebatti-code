array = []


with open("C:\Work Python\Eyler\Python file 11 eyler.txt", "r") as file1:
    for line1 in file1:
        row = []
        for char in line1.split():
            row.append(int(char))
        print(row)
        array.append(row)
file1.close()
print(array)

        #     Array.append(res)
        #     res = []
        #     continue
        # chislo += elem
        # if len(chislo) == 2:
        #     n = int(chislo)
        #     res.append(n)
        #     chislo = ""


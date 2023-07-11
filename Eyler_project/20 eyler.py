res = 1
A = []
for i in range(2,101):
    maxi = i*(i-1)
    res *= i
res = str(res)
A = list(res)
res = [int(elem) for elem in A if elem.isdigit()]
print(sum(res))


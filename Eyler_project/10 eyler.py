import math
# h = 9.6
# m=math.sqrt(h)
# print(m)
g=2
for i in range(3,2000000,2):
    m = math.sqrt(i)
    h = math.ceil(m)
    for j in range(2,(h+1)):
        if i % j == 0:
            break
    else:
        g=g+i
        print(i)
print(g)
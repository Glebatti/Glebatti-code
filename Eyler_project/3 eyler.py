a = 600851475143
for i in range(2,a):
    count = 0
    for n in range(2,i):
        if i % n==0:
            count=1
            break
    if count==0 and a % i==0:
        print(i)




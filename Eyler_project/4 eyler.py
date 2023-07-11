A=[]
M=[]
x=0
maxi=0
for i in range(2,1000):
    for j in range(2,1000):
        sum=i*j
        sum=str(sum)
        A=list(sum)
        M=list(reversed(A))
        # print(A)
        # for m in range(0,len(A)):
        if len(A)>1 and A==M:
            n=A
            # x = max(len(n))
            x=int("".join(n))
            if maxi < x:
                maxi=x
print(maxi)



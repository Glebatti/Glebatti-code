j=1
mini=0
# for m in range(2,10000):
m=0
# while m<10000 or j==9:
#     j=0
#     m+=1
#     for i in range(2,21):
#         if m % i==0:
#             j+=1
#         else:
#             break
#         if j==9:
#             print(m)
while j<21:
    j=0
    m+=1
    for i in range(2,30):
        if m % i==0:
            j+=1
        else:
            break
print(m)


# A=6739
# x=str(A)
# M=list(x)
# result = [A for A in M]
# print(M)
# print(result)



# k=0
# A=[]
# for j in range(1,11):
#     A.append(j)
# for n in range(0,9):
#     k=A[n]+A[n+1]
#     m=k+A[n+1]
#     y=m+k
#     # print()

# k=0
# r=1
# count=0
# for j in range(1,11):
#     for m in range(1,11):
#         if j<m and count<2:
#             k=j+m
#             count+=1
#             print(k)
#             break
#         if count>=2:
#             r=k+m
#             print(r)
a=1
b=2
r=2
sum=0
#print(a)
#print(b)
while sum < 4000000:
    #print(b)
    sum=a+b
    b=sum
    a=b-a
    if sum % 2 == 0:
        r=r+b
print(r)








# A = []
# def kollac(n):
#     A.append(n)
#     while n > 1:
#         if n % 2 == 0:
#             n = n//2
#             A.append(n)
#         else:
#             n = 3*n+1
#             A.append(n)
#         if len(A) > 250:
#             print(A)
# # for m in range (1000000,1,-1):
# kollac(8000)
# print(A, sep=' ')
# print(len(A))


for n in range(999999, 0, -1):
    A = []
    A.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n//2
            A.append(n)
        else:
            n = 3*n+1
            A.append(n)
    if len(A) > 524:
        print(A)
        print(len(A))





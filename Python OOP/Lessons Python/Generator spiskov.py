s=[(i, j) for i in range(1,21) for j in range(1,51)]

print(s)

s1 = [i ** 3 for i in range(1,21) if i % 5 ==0]
print(sum(s1))

s3 =[i ** 2
     if i > 0
     else i ** 3
     for i in range(-10,11)
     if i % 2 ==0]
print(s3)


s = [7,8,8,-10,-10]
set_set = {i for i in s}
print(set_set)
dictionary = {i:i**10 for i in s}
print(dictionary)

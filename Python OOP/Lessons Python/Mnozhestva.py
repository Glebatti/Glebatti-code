numbers = set([1, 1, 2, 5, 2])
print(numbers)
num = {1,2,3,4,5,6,7}
num2 = {8,2,35,46,53,65,7}
num3 = num | num2
num4 = num2 - num
print(num4)
num5 = num2.copy()
print(len(num5))
num.add(99)
TTT = list(num)
print(TTT)

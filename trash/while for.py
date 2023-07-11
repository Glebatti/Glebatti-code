# count=1
# while count<=5:
#     print(count)
#     count +=1

# while True:
#         value = input("Intenger,please[q to quit]:")
#         if value =="q":    #выход
#             break
#         number = int(value)
#         if number % 2 == 0: #нечетное число
#             continue
#         print(number,"squared is",number*number)

numbers = [1,2,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number",number)
        break
    position +=1
else:
        print("No even number found")


word = "thxd"
for letter in word:
    if letter =="x":
        print("EEk? An 'X'")
        break
    print(letter)
else:
    print("No x in there")

for x in range(0,3):
    print(x)
    print(list(range(0,3)))

for x in range(2,-1,-1):
    print(x)
    print(list(range(0,11,2)))

for r in range(3,-1,-1):
    print(list(range(3,-1,-1)))
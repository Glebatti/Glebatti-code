with open("1.txt","a") as f:
    f.write("   буга")
try:
    a = int(input("A:  "))
    b = int(input("B:  "))
    print(a / b)
except ZeroDivisionError:
    print("На 0 делить нельзя")

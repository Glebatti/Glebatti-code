q = ['zero','one','two','three','four','five','six','seven','eight', 'nine']
x = 1
s = int(input("Input figure : "))
low = s - 1
high = s + 5

while x <= 50:
    m = x
#    if not x % 10:
#        print(x)
    if ( low < m < high ) or ( x % 10==0 ):
        print(q[m%10])

        print(q[(m - 1) % 10])
    x += 1
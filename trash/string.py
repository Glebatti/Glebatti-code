#print("hello america")
#help("keywords")
a=7
print(a)
b=a
print(b)
print(type("ffff"))
print(isinstance(7,int))
two=deu=one=2
print(one)
x=5
y=x
x=29
print(x)
print(y)
a=[2,4,5]
b=a
print(a)
print(b)
a[0]=99
print(a)
print(b)
print(5+2.0)
print(bool(0))
a=10
a-=4
print(a)
9%5
print(divmod(9,5))
a=3
a*=3
print(a)
2.0**3
print(2.0**3)
value=65
print(bin(value))
print(hex(value))
print(int(True))
print(True+1+1)
x=60*60
print(x)
seconds_per_hour=x
seconds_per_day=seconds_per_hour/60
print(seconds_per_day)
y=seconds_per_hour/seconds_per_day
z=seconds_per_hour//seconds_per_day
print(y)
print(z)
sum=(
    1+
    2+
    3+
    4)
print(sum)
disaster=False
if disaster:
        print("woe")
else:
        print("whee")
furry=True
large=False
if furry:
    if large:
        print("yeti")
    else:
        print('cat')
else:
    if large:
        print('whale')
    else:
        print("human")
color="red"
if color =="red":
    print("tomato")
elif color =="green":
    print('paper')
elif color =="bee purple":
    print("i dont know")
else:
    print("i never heard of the color",color)
x=7
print(5>x or x>10)
print(5>x and not x<10)
vowels = 'aeiou'
letter ='a'
letter in vowels
if letter in vowels:
    print(letter,'is a vowel')
    letter = "a"
    vowel_set = {'a': 'apple' ,"e":"elephant","i":'impala',"o":'ocelot',"u":'unicorn'}
    print(letter in vowel_set)
if letter in vowel_set:
    print(letter,"is a vov")
    tweet_limit = 190
    tweet_string = "blah"*50
    if diff := tweet_limit- len(tweet_string) >=0:
        print("A fitting tweet")
    else:
        print("Went over by",abs(diff))
secret=7
guess=7
if guess<7:
    print('too low')
elif guess>7:
    print("too high")
elif guess == secret:
    print("just right")
else:
    print("nothing")
    str(True)
palin = "A man,\nA plan,\nA canal:\nPanama"
print(palin)
print("a\tabc")
print("try" + " no wait")
start="na"*4+"\n"
middle="hey"*3+"\n"
end="Goodbye"
print(start+start+middle+end)
letters="rtkhmspogjiht"
print(letters[-3])
print(letters.replace("r", "P"))
print(letters[10:12])
print(letters[4:-3])
print(letters[-3:])
print(letters[2::4])
print(len(letters))
tasks="get gloves,get mask,give cat,call ambu"
print(tasks.split())
crypto_list=["yety","bigfoot","loss"]
crypto_string= "yyyyyyyyyy".join(crypto_list)
print(crypto_string)
setup="a duck goes into a bar"
print(setup.replace("duck","marmoset"))
world="earth^*^ ttt"
print(world.strip("^*^"))
print((world.startswith('aa')))
print(world.capitalize())
print(world.title())
print(world.swapcase())
song='When an ell grabs your ascrm a moray'
print(song.title())
print(song.capitalize())
print(song.replace("When","moray"))
print(song.capitalize())
cyy=song.split()
print(cyy[7].capitalize())
print(cyy)
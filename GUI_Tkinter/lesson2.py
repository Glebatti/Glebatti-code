import random
import tkinter as tk

cn = 1


def say_hello():
    global cn
    cn += 1
    if cn % 2 == 0:
        btn2['state'] = tk.DISABLED
        btn3['state'] = tk.DISABLED
        btn4['state'] = tk.DISABLED
        btn5['state'] = tk.DISABLED
    if cn % 2 == 1:
        btn2['state'] = tk.NORMAL
        btn3['state'] = tk.NORMAL
        btn4['state'] = tk.NORMAL
        btn5['state'] = tk.NORMAL


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'

def color():
    global count
    count = random.randint(1,5)
    print(count)
    color = {1:'blue',
             2:'green',
             3:'white',
             4:'black',
             5:'yellow'}
    win.config(background=color[count])

count = 0

win = tk.Tk()
win.title('Мое первое графическое приложение')
h = 400
w = 500
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.geometry(f"{h}x{w}+100+200")

btn1 = tk.Button(win, text='Hello',
                 command=say_hello
                 )
btn2 = tk.Button(win, text='Add new label',
                 command=add_label
                 )

btn3 = tk.Button(win, text='Add new label lambda',
                 command=lambda: tk.Label(win, text='new lambda').pack())

btn4 = tk.Button(win, text=f'Счетчик: {count}',
                 command=counter,
                 activebackground='blue',
                 bg='red',
                 state=tk.NORMAL)

btn5 = tk.Button(win, text='Color',
                 command=color
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

win.mainloop()

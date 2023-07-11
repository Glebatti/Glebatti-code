import tkinter as tk

win = tk.Tk()

win.title('Мое первое графическое приложение')
h = 300
w = 400
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
# win.config(background='#2187EE')
win.geometry(f"{h}x{w}+100+200")
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)
label_1 = tk.Label(win, text='''Hello!
world!''',
                   bg='red',
                   fg='white',
                   font=('Arial', 15, 'bold'),
                   padx=20,
                   pady=40,
                   width=20,
                   height=10,
                   anchor='sw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )
label_1.pack()
win.mainloop()

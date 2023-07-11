import tkinter as tk

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Мое первое граффическое приложение')

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column=j, stick='we')


win.columnconfigure(0, minsize=200)
win.columnconfigure(1, minsize=100)
win.mainloop()

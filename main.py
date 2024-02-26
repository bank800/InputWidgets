from tkinter import *

App = Tk()
App.title('Entry')
App.geometry('350x100')

inp = Entry(App)
inp.pack()


def show():
    INP = inp.get()
    msg = Label(App, text=INP)
    msg.pack()


B = Button(App, text='Show', command=show)
B.pack()

App.mainloop()

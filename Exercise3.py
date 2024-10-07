from tkinter import *


class MyWindow:
    def __init__(self,win):

            #common widget
            win.configure(bg = "#f7eabf")
            self.Label1 = Label(win, fg="White", text="Calculator",bg = "#f7eabf",  font = ("Times New Roman", 40, "bold"))
            self.Label1.place(x=160, y=50)


            self.Label2 = Label(win, fg="Blue", text="Number 1: ",bg = "#f7eabf", font = ("Times New Roman", 20))
            self.Label2.place(x=80, y=200)
            self.Entry2 = Entry(win, bd=4)
            self.Entry2.place(x=80, y=230)

            self.Label3=Label(win,fg="Red", text="Number 2: ",bg = "#f7eabf",  font = ("Times New Roman", 20))
            self.Label3.place(x=80,y=300)
            self.Entry3 = Entry(win, bd=4)
            self.Entry3.place(x=80, y=340)

            self.Label4=Label(win,fg="Red", text="Results: ",bg = "#f7eabf", font = ("Times New Roman", 20))
            self.Label4.place(x=80, y=400)
            self.Entry4 = Entry(win, bd=4)
            self.Entry4.place(x=80, y=440)

            self.Button1 = Button(win, text="Add", width=5, height=3)
            self.Button1.grid(row = 0, column = 0)
            self.Button1.place(x =340, y = 160)
            self.Button1.bind('<Button-1>',self.add)

            self.Button2 = Button(win, text="Sub", width=5, height=3)
            self.Button2.grid(row=0, column=0)
            self.Button2.place(x=340, y=240)
            self.Button2.bind('<Button-1>', self.sub)

            self.Button3 = Button(win, text="Multi", width=5, height=3)
            self.Button3.grid(row=0, column=0)
            self.Button3.place(x=400, y=160)
            self.Button3.bind('<Button-1>', self.multi)

            self.Button4 = Button(win, text="Divide", width=5, height=3)
            self.Button4.grid(row=0, column=0)
            self.Button4.place(x=400, y=240)
            self.Button4.bind('<Button-1>', self.divide)

    def add(self,win):
        num1 = int(self.Entry2.get())
        num2 = int(self.Entry3.get())
        result= num1 + num2
        self.Entry4.insert(0,str(result))

    def sub(self, win):
        num1 = int(self.Entry2.get())
        num2 = int(self.Entry3.get())
        result = num1 - num2
        self.Entry4.insert(0, str(result))

    def multi(self, win):
        num1 = int(self.Entry2.get())
        num2 = int(self.Entry3.get())
        result = num1 * num2
        self.Entry4.insert(0, str(result))

    def divide(self, win):
        num1 = int(self.Entry2.get())
        num2 = int(self.Entry3.get())
        result = num1 / num2
        self.Entry4.insert(0, str(result))


window=Tk()
MyWin=MyWindow(window)
window.geometry("510x550+10+10")
window.title("Standard Calculator")
window.mainloop()

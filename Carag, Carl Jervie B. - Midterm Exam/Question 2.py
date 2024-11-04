# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:03:21 2024

@author: TIPQC
"""

from tkinter import *


class MyWindow:

    def __init__(self,win):

            #common widget
            win.configure(bg = "white")
            

            self.Button1 = Button(win, text="Click to change color", width=25, height=7, bg = "white")
            self.Button1.grid(row = 0, column = 0)
            self.Button1.place(x= 100,y=70)
            self.Button1.bind('<Button-1>', self.changecolor)
    
    def changecolor(self,win):
        self.Button1 = Button(win, text="Click to change color", width=25, height=7, bg = "yellow")
        

          
          
 
window=Tk()
MyWin=MyWindow(window)
window.geometry("510x550+10+10")
window.title("Spcecial Midterm Exam in OOP")
window.mainloop() 
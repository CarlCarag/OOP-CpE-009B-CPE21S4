# -*- coding: utf-8 -*-
import sys 
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon 

class App(QWidget): 
    def __init__(self):
        super().__init__() #intitializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "Midterm Exam in OOP"
        self.x=200 # or left 
        self.y=200 # or top
        self.width=400
        self.height=400
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('.ico'))
        
        #Create Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(180, 20)
        self.textbox.resize(180, 30)
        self.textbox.setText(" ")
        self.textboxlbl = QLabel("Enter your Fullname ", self)
        self.textboxlbl.move(10,25)
        
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 60)
        self.textbox2.resize(180, 30)
        self.textbox2.setText(" ")
        self.button = QPushButton('Click to display your fullname: ', self)
        self.button.setToolTip("you've hovered over me!")
        self.button.move(10,65) #button.move(x,y)
     
        
        
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
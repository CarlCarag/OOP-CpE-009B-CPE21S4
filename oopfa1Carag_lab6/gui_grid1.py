# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:01:55 2024

@author: TIPQC
"""


import sys 
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit,QGridLayout, QLabel
from PyQt5.QtGui import QIcon  



class App(QWidget): 
    def __init__(self):
        super().__init__() #intitializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "PyQt Button"
        self.x=200 # or left 
        self.y=200 # or top
        self.width=300
        self.height=300
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico')) 
        
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()
    
    def createGridLayout(self):
        self.layout = QGridLayout()
        
        self.layout.setColumnStretch(1,2)
        self.textboxlbl = QLabel("Text: ", self)
        self.textbox = QLineEdit(self)
        self.passwordlbl = QLabel("Password: ", self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.button = QPushButton('Register', self)
        self.button.setToolTip("You 've Hovered over me!")
        self.layout.addWidget(self.textboxlbl,0,1)
        self.layout.addWidget(self.textbox,0,2)
        self.layout.addWidget(self.passwordlbl,1,1)  
        self.layout.addWidget(self.password,1,2)
        self.layout.addWidget(self.button,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
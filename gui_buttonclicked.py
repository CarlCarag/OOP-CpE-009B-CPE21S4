# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:10:15 2024

@author: TIPQC
"""

import sys 
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton 
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
        
        
        #In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("you've hovered over me!")
        self.button.move(100,70) #button.move(x,y)
        self.button.clicked.connect (self.on_click)
    
        
        
        self.show()
        
    @pyqtSlot() 
    def on_click(self):
        print('You Clicked Me!')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
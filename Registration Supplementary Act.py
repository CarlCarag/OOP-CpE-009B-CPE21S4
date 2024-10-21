# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:47:06 2024

@author: TIPQC
"""

import sys 
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QMessageBox 
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import pyqtSlot 

class App(QWidget): 
    def __init__(self):
        super().__init__() #intitializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "Account Registration"
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
        self.textbox.move(80, 20)
        self.textbox.resize(180, 30)
        self.textbox.setText(" ")
        self.textboxlbl = QLabel("First Name ", self)
        self.textboxlbl.move(10,25)
        
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(80, 60)
        self.textbox2.resize(180, 30)
        self.textbox2.setText(" ")
        self.textboxlbl2 = QLabel("Last Name ", self)
        self.textboxlbl2.move(10,65)
        
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(80, 100)
        self.textbox3.resize(180, 30)
        self.textbox3.setText(" ")
        self.textboxlbl3 = QLabel("Username ", self)
        self.textboxlbl3.move(10,105)
        
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(80, 140)
        self.textbox4.resize(180, 30)
        self.textbox4.setText(" ")
        self.textboxlbl4 = QLabel("Password ", self)
        self.textboxlbl4.move(10,145)
        
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(80, 180)
        self.textbox5.resize(200, 30)
        self.textbox5.setText(" ")
        self.textboxlbl5 = QLabel("Email Address ", self)
        self.textboxlbl5.move(10,185)
        
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(90, 220)
        self.textbox6.resize(200, 30)
        self.textbox6.setText(" ")
        self.textboxlbl6 = QLabel("Contact Number ", self)
        self.textboxlbl6.move(10,225)
        
        self.buttonS = QPushButton('Submit', self) 
        self.buttonS.move(80,280) #button.move(x,y)
        self.buttonS.clicked.connect(self.on_click)
        
        self.button2 = QPushButton('Clear', self) 
        self.button2.move(180,280) #button.move(x,y)
        
        
    @pyqtSlot() 
    def on_click(self):
        buttonReply = QMessageBox.question(self, "Files Pending", "Do you like to submit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes: 
            QMessageBox.warning(self, "Evaluation", "Files Successfully Submitted", QMessageBox.Ok,QMessageBox.Ok)
        
        else:
            QMessageBox.information(self, "Evaluation", "Files Not Successfully Submitted", QMessageBox.Ok, QMessageBox.Ok)     
            
        
        
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  
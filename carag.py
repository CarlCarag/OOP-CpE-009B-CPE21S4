# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:57:59 2024

@author: TIPQC
"""
import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon 


class App(QMainWindow): 


    def __init__(self): 
        super(). __init__() #intitializes the main window like in the previous one
        # window = MainWindow()
        self.title = "First OOP GUI"
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,300,300)
        self.setWindowIcon(QIcon('pythonico.ico')) #sets an icon
        self.show

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:01:13 2024

@author: TIPQC
"""

from FileReaderWriter import FileReaderWriter 
import csv 

class TextFileReaderWriter(FileReaderWriter): 
    def read(self, filepath):
        with open(filepath, newline='') as csvfile: 
            data = csv.reader(csvfile, delimiter= ',', quotechar='/')
            for row in data:
                print(row)
            return data 
    
    def write(self,filepath,data):
        with open(filepath, 'w', newline='') as csvfile:
            writer=csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
            
            writer.writerow(data)                   
                              
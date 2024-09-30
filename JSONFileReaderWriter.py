# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:14:37 2024

@author: TIPQC
"""

from FileReaderWriter import FileReaderWriter 
import json 

class JSONFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath,"r",)as read_file: 
            data=json.load(read_file)
            print(data) 
            return(data)
    def write(self, filepath, data):
            with open(filepath, "w") as write_file:
                    json.dump(obj=data, fp=write_file)
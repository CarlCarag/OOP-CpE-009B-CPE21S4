# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:01:29 2024

@author: TIPQC
"""

def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32


 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15


 class FahrenheitToCelsius(TemperatureConversion): #Class for Fahrenheit to Celsius
  def conversion(self): # defined function used to initiate the conversion of Fahrenheit to Celsius
   return ((self._temp - 32)* 5/9) # The operation of Fahrenheit to Celsius
 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit to Celsius: ")) #The user enters the amount of the value of Fahrenheit
 convert = FahrenheitToCelsius(tempInFahrenheit) #Calls the function initiated 
 print(str(convert.conversion()) + " Celsius")


 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return ((self._temp - 32)* 5/9)
 tempInKelvin = float(input("Enter the temperature in Kelvin to Celsius: "))
 convert = KelvinToCelsius(tempInKelvin)
 print(str(convert.conversion()) + " Celsius")
 
 
 tempInCelsius = float(input("Enter the temperature in Celsius : "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 
 
 
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")


main() 
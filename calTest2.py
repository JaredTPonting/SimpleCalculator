# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:01:22 2020

@author: jared
"""



num1 = float(input("First Number :"))
operator = input("Operator (+, -, *, /): ")
num2 = float(input("Second Number: "))



out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))
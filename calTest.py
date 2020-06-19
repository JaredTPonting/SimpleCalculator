# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:48:37 2020

@author: jared
"""


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y


print("select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    # take input from user
    choice = input("Enter operation choice:")
    if choice in ("1","2","3","4"):
        num1 = float(input("Enter first Number:"))
        num2 = float(input("Enter second number:"))
        if choice == "1":
            print(num1, "+", num2,"=", add(num1,num2))
        elif choice == "2":
            print(num1, "-", num2,"=", subtract(num1,num2))
        elif choice == "3":
            print(num1, "x", num2,"=", multiply(num1,num2))
        elif choice == "4":
            print(num1, "/", num2, divide(num1,num2))
        break
    else:
        print("Invalid Input")
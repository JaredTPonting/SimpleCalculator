# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:28:27 2020

@author: jared
"""


import tkinter as tk
HEIGHT = 500
WIDTH = 500

def clear():
    entry.delete(0, tk.END)
    
def buttonDo(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(2, current + str(number))
    
def buttonAdd():
    fNum = entry.get()
    global first
    first = float(fNum)
    clear()
    global Mult
    global addition
    global Sub
    global Div
    addition = True
    Mult = False
    Sub = False
    Div = False
    
def buttonMul():
    fNum = entry.get()
    global first
    first = float(fNum)
    clear()
    global Mult
    global addition
    global Sub
    global Div
    Mult = True
    Div = False
    addition = False
    Sub = False
    
def buttonDiv():
    fNum = entry.get()
    global first
    first = float(fNum)
    clear()
    global Mult
    global addition
    global Sub
    global Div
    Mult = False
    Div = True
    addition = False
    Sub = False
def buttonSub():
    fNum = entry.get()
    global first
    first = float(fNum)
    clear()
    global Mult
    global addition
    global Sub
    global Div
    Mult = False
    Div = False
    addition = False
    Sub = True

def Eq():
    sNum = entry.get()
    second = float(sNum)
    global ans
    if addition:
        ans = first + second
        clear()
        entry.insert(0,ans)
    elif Mult:
        ans = first * second
        clear()
        entry.insert(0,ans)
    elif Div:
        ans = first / second
        clear()
        entry.insert(0,ans)
    elif Sub:
        ans = first - second
        clear()
        entry.insert(0,ans)

root = tk.Tk()
root.title("Calculator")






canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame1 = tk.Frame(root,bd = 5, bg = "light grey")
frame1.place(relx = 0, rely = 0, relheight = 0.2, relwidth = 1)
frame2 = tk.Frame(root,bd = 0.1, bg = "green")
frame2.place(relx = 0, rely = 0.2, relheight = 0.2, relwidth = 1)
frame3 = tk.Frame(root,bd = 0.1, bg = "red")
frame3.place(relx = 0, rely = 0.4, relheight = 0.2, relwidth = 1)
frame4 = tk.Frame(root,bd = 0.1, bg = "green")
frame4.place(relx = 0, rely = 0.6, relheight = 0.2, relwidth = 1)
frame5 = tk.Frame(root,bd = 0.1, bg = "red")
frame5.place(relx = 0, rely = 0.8, relheight = 0.2, relwidth = 1)


entry = tk.Entry(frame1)
entry.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
#label = tk.Label(frame1, bg = "white")
#label.place(relx=0,rely=0,relwidth=1,relheight=1)

button7 = tk.Button(frame2, text = "7", command = lambda: buttonDo(7))
button7.place(relx = 0, rely = 0, relwidth = 0.25, relheight = 1)
button8 = tk.Button(frame2, text = "8", command = lambda: buttonDo(8))
button8.place(relx = 0.25, rely = 0, relwidth = 0.25, relheight = 1)
button9 = tk.Button(frame2, text = "9", command = lambda: buttonDo(9))
button9.place(relx = 0.5, rely = 0, relwidth = 0.25, relheight = 1)

button4 = tk.Button(frame3, text = "4", command = lambda: buttonDo(4))
button4.place(relx = 0, rely = 0, relwidth = 0.25, relheight = 1)
button5 = tk.Button(frame3, text = "5", command = lambda: buttonDo(5))
button5.place(relx = 0.25, rely = 0, relwidth = 0.25, relheight = 1)
button6 = tk.Button(frame3, text = "6", command = lambda: buttonDo(6))
button6.place(relx = 0.5, rely = 0, relwidth = 0.25, relheight = 1)

button1 = tk.Button(frame4, text = "1", command = lambda: buttonDo(1))
button1.place(relx = 0, rely = 0, relwidth = 0.25, relheight = 1)
button2 = tk.Button(frame4, text = "2", command = lambda: buttonDo(2))
button2.place(relx = 0.25, rely = 0, relwidth = 0.25, relheight = 1)
button3 = tk.Button(frame4, text = "3", command = lambda: buttonDo(3))
button3.place(relx = 0.5, rely = 0, relwidth = 0.25, relheight = 1)


button0 = tk.Button(frame5, text = "0", command = lambda: buttonDo(0))
button0.place(relx = 0, rely = 0, relwidth = 0.25, relheight = 1)
buttonDecimal = tk.Button(frame5, text = ".", command = lambda: buttonDo("."))
buttonDecimal.place(relx = 0.25, rely = 0, relwidth = 0.25, relheight = 1)
buttonEq = tk.Button(frame5, text = "=", command = Eq)
buttonEq.place(relx = 0.5, rely = 0, relwidth = 0.25, relheight = 0.5)

buttonDivide = tk.Button(frame2, text = "/", command = buttonDiv)
buttonDivide.place(relx = 0.75,rely=0, relwidth = 0.25, relheight = 1)

buttonMultiply = tk.Button(frame3, text = "x", command = buttonMul)
buttonMultiply.place(relx = 0.75,rely=0, relwidth = 0.25, relheight = 1)

buttonSub = tk.Button(frame4, text = "-", command = buttonSub)
buttonSub.place(relx = 0.75,rely=0, relwidth = 0.25, relheight = 1)

buttonAdd = tk.Button(frame5, text = "+", command = buttonAdd)
buttonAdd.place(relx = 0.75,rely=0, relwidth = 0.25, relheight = 1)

buttonBack = tk.Button(frame5, text = "Clear", command = clear)
buttonBack.place(relx = 0.5, rely = 0.5, relwidth = 0.25, relheight = 0.5)




root.mainloop()
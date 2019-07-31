import tkinter as tk
from tkinter import *
from math import *
main = tk.Tk()
main.title('CALCULATOR')
def add():
	Ans =int(num2.get())+int(num1.get())
	blank.insert(100,Ans)
def subtract():
	Ans =int(num2.get())-int(num1.get())
	blank.insert(100,Ans)
def multiply():
	Ans =int(num2.get())*int(num1.get())
	blank.insert(100,Ans)
def divide():
	Ans =int(num2.get())/int(num1.get())
	blank.insert(100,Ans)
main.title('counting seconds')
button = tk.Button(main,text='+', width=12, command=add)
button.grid(row=3, column=0)
button = tk.Button(main,text='-', width=12, command=subtract)
button.grid(row=3, column=1)
button = tk.Button(main,text='X', width=12, command=multiply)
button.grid(row=4, column=0)
button = tk.Button(main,text='/', width=12, command=divide)
button.grid(row=4, column=1)

main.geometry('225x150')
Label(main, text = "Enter Num 1:").grid(row=0)
Label(main, text = "Enter Num 2:").grid(row=1)
Label(main, text = "The Answer is:").grid(row=2)

num1=Entry(main)
num2=Entry(main)
blank=Entry(main)

num2.grid(row=0, column=1)
num1.grid(row=1, column=1)
blank.grid(row=2, column=1)
main.mainloop()
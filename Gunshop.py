import tkinter as tk
from tkinter import messagebox as msg
win = tk.Tk()
win.title("Gunshop")
win.geometry("900x500")
tk.Label(win, bg="gray", fg="white",width=200,height=5).place(x=5,y=10)
tk.Label(win,text="WELCOME TO GUN SHOP",bg="gray",fg="white",font="arial 15 bold").place(x=340,y=10)
tk.Label(win,text="Please Choose Your Gun Type:",fg="black",font="system").place(x=350,y=100)
button1 = tk.Button(win,text="HAND GUN",font="arial 13 bold").place(x=20,y=200)
button2 = tk.Button(win,text="SHUTGUN",font="arial 13 bold").place(x=250,y=200)
button3 = tk.Button(win,text="SNIPER",font="arial 13 bold").place(x=490,y=200)
button4 = tk.Button(win,text="RIFLE",font="arial 13 bold").place(x=750,y=200)
win.mainloop()
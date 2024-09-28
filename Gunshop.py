import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image

win = tk.Tk()
win.title("Gunshop")
win.geometry("1030x500")

tk.Label(win, bg="gray", fg="white", width=200, height=5).place(x=5, y=10)
tk.Label(win, text="WELCOME TO GUN SHOP", bg="gray", fg="white", font="arial 15 bold").place(x=360, y=10)
tk.Label(win, text="Please Choose Your Gun Type:", fg="black", font="system").place(x=390, y=100)

def load_image(path, size=(100, 100)):
    image = Image.open(path)
    return ImageTk.PhotoImage(image)

handgun_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\a.png")
shotgun_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\b.png")
sniper_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\c.png")
rifle_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\d.png")

button1 = tk.Button(win, text="HAND GUN", font="arial 13 bold").place(x=60, y=200)
button2 = tk.Button(win, text="SHOTGUN", font="arial 13 bold").place(x=300, y=200)
button3 = tk.Button(win, text="SNIPER", font="arial 13 bold").place(x=570, y=200)
button4 = tk.Button(win, text="RIFLE", font="arial 13 bold").place(x=850, y=200)

label1 = tk.Label(win, image=rifle_image,width=200).place(x=20, y=250)
label2 = tk.Label(win, image=sniper_image).place(x=250, y=250)
label3 = tk.Label(win, image=shotgun_image).place(x=490, y=250)
label4 = tk.Label(win, image=handgun_image).place(x=750, y=250)

win.mainloop()
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


def open_handgun_window():
    new_window = tk.Toplevel(win)
    new_window.title("Hand Gun")
    new_window.geometry("600x600")
    tk.Label(new_window, text="Hand Guns window", font="system 17").pack(pady=20)

    # بارگذاری تصاویر جدید
    handgun_img1 = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\gun1.png", size=(100, 100))
    handgun_img2 = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\gun2.png", size=(100, 100))
    handgun_img3 = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\gun3.png", size=(100, 100))

    # قرار دادن تصاویر به صورت ضربدری با استفاده از label ها
    tk.Label(new_window, image=handgun_img1).place(x=50, y=90)
    tk.Label(new_window, text="58.98$", font="arial 15 bold", bg="gray").place(x=100, y=240)
    tk.Label(new_window, text="SPRINGFIELD XDS"
                              ".45 ACP", font="system 12 bold").place(x=50, y=270)
    tk.Label(new_window, image=handgun_img2).place(x=350, y=100)
    tk.Label(new_window, text="60.0$", font="arial 15 bold", bg="gray").place(x=430, y=270)
    tk.Label(new_window, text="GLOCK 42"
                              ".380 ACP", font="system 12 bold").place(x=390, y=300)
    tk.Label(new_window, image=handgun_img3).place(x=40, y=360)
    tk.Label(new_window, text="100.95$", font="arial 15 bold", bg="gray").place(x=90, y=520)
    tk.Label(new_window, text="CLOCK 19"
                              "9MM", font="system 12").place(x=90, y=560)

    # نگه داشتن مرجع تصویرها
    new_window.handgun_img1 = handgun_img1
    new_window.handgun_img2 = handgun_img2
    new_window.handgun_img3 = handgun_img3


def open_shotgun_window():
    new_window = tk.Toplevel(win)
    new_window.title("Shotgun")
    new_window.geometry("600x600")
    tk.Label(new_window, text="Shotguns window", font="system 17").pack(pady=20)
    # بارگذاری تصاویر جدید

    shutgun_img1 = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\shotgun3.png", size=(100, 100))
    shutgun_img2 = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\shotgun2.png", size=(100, 100))



    # قرار دادن تصاویر به صورت ضربدری با استفاده از label ها

    tk.Label(new_window, image=shutgun_img1).place(x=50,y=90)
    tk.Label(new_window,text="256.95$", font="arial 15 bold",bg="gray").place(x=250, y=200)
    tk.Label(new_window,text="MOSSBERG 500",font="System 12").place(x=50,y=190)
    tk.Label(new_window,image=shutgun_img2).place(x=50,y=260)
    tk.Label(new_window,text="300.0$", font="arial 15 bold",bg="gray").place(x=340,y=370)
    tk.Label(new_window,text="BENELLI M4",font="System 12").place(x=50,y=370)

    # نگه داشتن مرجع تصویرها
    new_window.shutgun_img1 = shutgun_img1
    new_window.shutgun_img2 = shutgun_img2





def open_sniper_window():
    new_window = tk.Toplevel(win)
    new_window.title("Sniper")
    new_window.geometry("600x600")
    tk.Label(new_window, text="Snipers window", font="system 17").pack(pady=20)


def open_rifle_window():
    new_window = tk.Toplevel(win)
    new_window.title("Rifle")
    new_window.geometry("600x600")
    tk.Label(new_window, text="Rifles window", font="system 17").pack(pady=20)


handgun_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\a.png")
shotgun_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\b.png")
sniper_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\c.png")
rifle_image = load_image(r"C:\Users\Ali\PycharmProjects\GunShop\images\d.png")

button1 = tk.Button(win, text="HAND GUN", font="arial 13 bold", command=open_handgun_window).place(x=60, y=200)
button2 = tk.Button(win, text="SHOTGUN", font="arial 13 bold", command=open_shotgun_window).place(x=300, y=200)
button3 = tk.Button(win, text="SNIPER", font="arial 13 bold", command=open_sniper_window).place(x=570, y=200)
button4 = tk.Button(win, text="RIFLE", font="arial 13 bold", command=open_rifle_window).place(x=850, y=200)

label1 = tk.Label(win, image=rifle_image, width=200).place(x=20, y=250)
label2 = tk.Label(win, image=sniper_image).place(x=250, y=250)
label3 = tk.Label(win, image=shotgun_image).place(x=490, y=250)
label4 = tk.Label(win, image=handgun_image).place(x=750, y=250)

win.mainloop()

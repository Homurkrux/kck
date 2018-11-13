from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
def info():
    messagebox.showinfo("Informacje","ja jestem autorem programu")
def cover1():

    plotno.create_image(200,200,image=obraz1Tk)


def cover2():
    plotno.create_image(200,200,image=obraz2Tk)

def cover3():
    plotno.create_image(200,200,image=obraz3Tk)
glowneOkno=Tk()
wartosc=IntVar()
glowneOkno.title("Tk")
glowneOkno.geometry("700x700")
pasekmenu=Menu(glowneOkno)
mojemenu=Menu(pasekmenu, tearoff=0)
mojemenu.add_command(label="Info",command=info)
mojemenu.add_command(label="Wyjdz",command=glowneOkno.quit)
pasekmenu.add_cascade(label="pierwsze", menu=mojemenu)
glowneOkno.config(menu=pasekmenu)

plotno=Canvas(glowneOkno, width=600, height=600)
plotno.place(x=150,y=100)

obraz1= Image.open("cover1.jpg")
obraz1= obraz1.resize((200,200))
obraz1Tk=ImageTk.PhotoImage(obraz1)
obraz2= Image.open("cover2.jpg")
obraz2= obraz2.resize((200,200))
obraz2Tk=ImageTk.PhotoImage(obraz2)
obraz3= Image.open("cover3.jpg")
obraz3= obraz3.resize((200,200))
obraz3Tk=ImageTk.PhotoImage(obraz3)
przycisk1=Radiobutton(glowneOkno,text="rysunek 1",variable=wartosc, value=1, command=cover1)
przycisk1.place(x=150, y=400)
przycisk2=Radiobutton(glowneOkno,text="rysunek 2",variable=wartosc, value=2, command=cover2)
przycisk2.place(x=300, y=400)
przycisk3=Radiobutton(glowneOkno,text="rysunek 3",variable=wartosc, value=3, command=cover3)
przycisk3.place(x=450, y=400)

glowneOkno.mainloop()

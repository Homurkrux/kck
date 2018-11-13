from tkinter import *
from tkinter import messagebox
glowneOkno=Tk()
wartosc=IntVar()
def akcjaPrzycisk():
    messagebox.showinfo("okno powitalne",poleTekstowe.get())
def akcja():
    if wartosc.get()==1:
        messagebox.showinfo("okno powitalne","Elko")
    if wartosc.get()==2:
        messagebox.showinfo("okno powitalne","KAPPA")
def akcjared():
    messagebox.showinfo("okno powitalne","red")
def akcjablue():
    messagebox.showinfo("okno powitalne","blue")
def akcjagreen():
    messagebox.showinfo("okno powitalne","green")
def akcjawhite():
    messagebox.showinfo("okno powitalne","White")
glowneOkno.title('Moje Okno')
glowneOkno.geometry("300x250")
opisPolaTekstowego = Label(glowneOkno,text='Wprowadz tekst:')
opisPolaTekstowego.grid(row=2, column=0)
poleTekstowe=Entry(glowneOkno)
poleTekstowe.grid(row=2, column=3)
przycisk1=Button(glowneOkno, text="Juz cos robie", command = akcjaPrzycisk)
przycisk1.grid(row=3, column=0)
przyciskCzerwony=Button(glowneOkno, text="Czerwony", fg="red", command = akcjared)
przyciskCzerwony.grid(row=0, column=0)
przyciskZielony=Button(glowneOkno, text="Zielony", fg="green", command = akcjagreen)
przyciskZielony.grid(row=0, column=1)
przyciskNiebieski=Button(glowneOkno, text="Niebieski", fg="blue", command = akcjablue)
przyciskNiebieski.grid(row=0, column=2)
przyciskBialy=Button(glowneOkno, text="Biały", fg="white",command = akcjawhite)
przyciskBialy.grid(row=1, column=0)
rprzycisk1=Radiobutton(glowneOkno, text="Wybor 1", variable=wartosc, value=1)
rprzycisk1.grid(row=4, column=0)
rprzycisk2=Radiobutton(glowneOkno, text="Wybor 2", variable=wartosc, value=2)
rprzycisk2.grid(row=4, column=2)
rprzycisk=Button(glowneOkno,text="akcja",command=akcja)
rprzycisk.grid(row=5, column=1)
glowneOkno.mainloop()

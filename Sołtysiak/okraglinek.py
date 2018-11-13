from tkinter import *
from tkinter import messagebox
glowneOkno=Tk()
glowneOkno.title('Moje Okno')
glowneOkno.geometry("300x250")
def wynik():
    messagebox.showinfo("okno powitalne",int(dlugosc.get())*int(wysokosc.get()))
wysokosc = Label(glowneOkno,text='podaj wysokosc:')
wysokosc.grid(row=0, column=0)
wysokosc=Entry(glowneOkno)
wysokosc.grid(row=0, column=3)
dlugosc = Label(glowneOkno,text='podaj dlugosc:')
dlugosc.grid(row=2, column=0)
dlugosc=Entry(glowneOkno)
dlugosc.grid(row=2, column=3)
przycisk=Button(glowneOkno, text="Pole", command = wynik)
przycisk.grid(row=5,column=2)
glowneOkno.mainloop()

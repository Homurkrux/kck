from tkinter import *
from tkinter import messagebox
def wysylamy():
    if pierwszaOdpowiedz.get()=="Poniedziałek" and drugaOdpowiedz.get()=="Wtorek" and trzeciaOdpowiedz.get()=="Środa":
        messagebox.showinfo("Informacja","Prawidłowa odpowiedź!")
    else:
        messagebox.showinfo("Informacja","Co najmniej jedna z odpowiedzi jest nieprawidłowa!")
glowneOkno=Tk()
glowneOkno.title("Buffalo")
glowneOkno.geometry("400x300")
pierwszePytanie = Label(glowneOkno,text='Jaki jest pierwszy dzien tygodnia')
pierwszePytanie.grid(row=0,column=0)
pierwszaOdpowiedz=Entry(glowneOkno)
pierwszaOdpowiedz.grid(row=0, column=1)
drugiePytanie = Label(glowneOkno,text='Jaki jest drugi dzień tygodnia:')
drugiePytanie.grid(row=1, column=0)
drugaOdpowiedz=Entry(glowneOkno)
drugaOdpowiedz.grid(row=1, column=1)
trzeciePytanie = Label(glowneOkno,text='Jaki jest trzeci dzień tygodnia:')
trzeciePytanie.grid(row=2, column=0)
trzeciaOdpowiedz=Entry(glowneOkno)
trzeciaOdpowiedz.grid(row=2, column=1)
wyslij=Button(glowneOkno,text="wyślij", command=wysylamy)
wyslij.grid(row=3, column=1)
glowneOkno.mainloop()

import tkinter as tk

from Control.CtPerson import CtPerson
from Control.CtSpent import CtSpent
from Control.CtTypeSpent import CtTypeSpent


def openSpent():
    control = CtSpent()
    control.initFormSpent()
def openTypeSpent():
    control = CtTypeSpent()
    control.initFormTypeSpent()
def openPerson():
    control=CtPerson()
    control.initFormPerson()

def openPaysheet():
    control=Ct
    control.initFormPerson()

main = tk.Tk()
main.configure(background='#6B97E8')
main.title("PANEL PRINCIPAL")
main.geometry("1000x1000")



boton_enviar = tk.Button(main, text="Panel Gastos", command=openSpent,height=10, width=15)
boton_enviar.grid(row=0, column=0)

boton_enviar = tk.Button(main, text="Panel Personas", command=openPerson,height=10, width=15)
boton_enviar.grid(row=1, column=0)

boton_enviar = tk.Button(main, text="Panel Tipo Gastos", command=openTypeSpent,height=10, width=15)
boton_enviar.grid(row=2, column=0)

boton_enviar = tk.Button(main, text="Panel Nominas", command=openPaysheet,height=10, width=15)
boton_enviar.grid(row=3, column=0)
main.mainloop()
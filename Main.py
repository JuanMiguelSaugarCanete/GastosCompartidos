import tkinter as tk

from View.ViewPaysheet import ViewPaysheet
from View.ViewPerson import ViewPerson
from View.ViewTypeSpent import ViewTypeSpent
from View.ViewSpent import ViewSpent


def openSpent():
    control = ViewSpent()
    control.initForm()
def openTypeSpent():
    control = ViewTypeSpent()
    control.initForm()
def openPerson():
    control=ViewPerson()
    control.initForm()

def openPaysheet():
    control=ViewPaysheet()
    control.initForm()

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
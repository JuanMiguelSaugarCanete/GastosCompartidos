import tkinter as tk
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from datetime import datetime

from Control.CtSpent import CtSpent


class ViewSpent:

    def __init__(self):
        self.form = tk.Tk()
        self.form.title("PANEL Gastos")
        self.form.geometry("1000x1000")
        self.initComponents()


    def initComponents(self):
        self.control = CtSpent()
        self.cal = Calendar(self.form)
        self.nombre = tk.Entry(self.form)
        self.typeSpent = tk.Entry(self.form)
        self.amount = tk.Entry(self.form)
        self.observation = tk.Entry(self.form)
        self.comboBoxType = ttk.Combobox(self.form, state="readonly")
        self.comboBoxTypeOperation = ttk.Combobox(self.form, state="readonly")
        self.tree = Treeview(self.form, columns=('ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación'))

    def addSpent(self):
        dateNow = None
        if (self.cal):
            dateNow = self.cal.get_date()
            dateNow = datetime.strptime(dateNow, '%m/%d/%y').strftime("%d-%m-%Y")
        else:
            dateNow = datetime.today().strftime("%d-%m-%Y")
        typeSpent = self.comboBoxType.get()
        name = self.nombre.get()
        amount = self.amount.get()
        observation = self.observation.get()
        self.control.addSpent()


    def initForm(self):
        tk.Label(self.form, text="Nombre Gasto:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.form)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.form, text="Tipo Gasto:").grid(row=1, column=0)
        self.getAllTypeSpent()
        tk.Label(self.form, text="Fecha del gasto:").grid(row=2, column=0)
        self.cal = Calendar(self.form)
        self.cal.grid(row=2, column=1)
        tk.Label(self.form, text="Cantidad:").grid(row=4, column=0)
        self.amount = tk.Entry(self.form)
        self.amount.grid(row=4, column=1)

        tk.Label(self.form, text="Observaciones:").grid(row=5, column=0)
        self.observation = tk.Entry(self.form)
        self.observation.grid(row=5, column=1)

        boton_enviar = tk.Button(self.form, text="Añadir", command=self.addSpent)
        boton_enviar.grid(row=6, column=0, columnspan=2)


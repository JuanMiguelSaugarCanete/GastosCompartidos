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
        self.control.addSpent(name, dateNow, typeSpent, amount, observation)

    def updateTable(self):
        self.tree.delete(*self.tree.get_children())
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Tipo')
        self.tree.heading('#4', text='Fecha')
        self.tree.heading('#5', text='Cantidad')
        self.tree.heading('#6', text='Observación')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        listSpent = self.control.getAllSpent()
        for gasto in listSpent:
            self.tree.insert('', 'end',
                             values=(
                                 gasto.id, gasto.name, gasto.typeSpentName, gasto.date, gasto.amount,
                                 gasto.observation))

        # Ajustar las columnas
        for col in ('#1', '#2', '#3', '#4', '#5', '#6'):
            self.tree.column(col, anchor='center')
        scrollbar = ttk.Scrollbar(self.form, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        # Mostrar la tabla
        self.tree.grid(row=7, column=10, padx=25, pady=15)


    def getAllSpent(self):
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation["values"] = operationOption
        tk.Label(self.form, text="Operacion:").grid(row=5, column=10)
        self.comboBoxTypeOperation.grid(row=6, column=10)

        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Tipo')
        self.tree.heading('#4', text='Fecha')
        self.tree.heading('#5', text='Cantidad')
        self.tree.heading('#6', text='Observación')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        listSpent = self.control.getAllSpent()
        for gasto in listSpent:
            self.tree.insert('', 'end',
                             values=(
                             gasto.id, gasto.name, gasto.typeSpentName, gasto.date, gasto.amount, gasto.observation))

        # Ajustar las columnas
        for col in ('#1', '#2', '#3', '#4', '#5', '#6'):
            self.tree.column(col, anchor='center')
        scrollbar = ttk.Scrollbar(self.form, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        # Mostrar la tabla
        self.tree.grid(row=7, column=10, padx=25, pady=15)

    def initForm(self):
        tk.Label(self.form, text="Nombre Gasto:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.form)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.form, text="Tipo Gasto:").grid(row=1, column=0)
        self.comboBoxType["values"] = self.control.getAllTypeSpent()
        self.comboBoxType.grid(row=1, column=1)
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

        self.getAllSpent()
        self.form.mainloop()


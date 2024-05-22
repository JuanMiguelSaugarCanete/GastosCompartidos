from datetime import datetime
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview

import tkinter as tk
from tkcalendar import Calendar

from Data.OperateSpent import OperateSpent
from Data.OperateTypeSpent import OperateTypeSpent
from Model.Spent import Spent
from util.Util import Util


class CtSpent:
    def __init__(self):
        self.listTypeSpent = []
        self.listSpent = []
        self.form = tk.Tk()
        self.form.title("PANEL Gastos")
        self.form.geometry("1000x1000")
        self.initComponents()
    def initComponents(self):
        self.cal = Calendar(self.form)
        self.nombre = tk.Entry(self.form)
        self.typeSpent = tk.Entry(self.form)
        self.amount = tk.Entry(self.form)
        self.observation = tk.Entry(self.form)
        self.comboBoxType = ttk.Combobox(self.form, state="readonly")
        self.comboBoxTypeOperation = ttk.Combobox(self.form, state="readonly")
        self.tree = Treeview(self.form, columns=('ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación'))
    def addSpent(self):
        unique_id = Util().generateUniqueId()
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

        idTypeSpent = OperateTypeSpent().getTypeSpentIdByName(typeSpent)

        spent = Spent(unique_id,name,idTypeSpent,dateNow,amount,observation)
        OperateSpent().addSpent(spent)
        #actualizar tabla

    def updateTable(self):
        self.tree.delete(*self.tree.get_children())
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Tipo')
        self.tree.heading('#4', text='Fecha')
        self.tree.heading('#5', text='Cantidad')
        self.tree.heading('#6', text='Observación')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.listSpent = OperateSpent().getAllSpent()
        for gasto in self.listSpent:
            self.tree.insert('', 'end',
                             values=(gasto.id, gasto.name, OperateTypeSpent().getTypeSpentNameById(gasto.typeSpentId),
                                     gasto.date, gasto.amount, gasto.observation))
        for col in ('#1', '#2', '#3', '#4', '#5', '#6'):
            self.tree.column(col, anchor='center')
        scrollbar = ttk.Scrollbar(self.form, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        # Mostrar la tabla
        self.tree.grid(row=7, column=10, padx=25, pady=15)
    def item_selected(self, event):
        selected_item = self.tree.focus()
        item = self.tree.item(selected_item)['values']
        operation = self.comboBoxTypeOperation.get()
        if (operation == "ELIMINAR"):
            resultado = messagebox.askyesno("Confirmación", "¿Deseas continuar con la acción?")
            if resultado:
                OperateSpent().deleteSpent(item[0])
                self.updateTable()

        elif (operation == "COPIAR"):
            print(f"Elemento copiado: {self.toString(item)}")

    def toString(self, list):
        return f"id del gasto: {list[0]} \n nombre del gasto: {list[1]} \n Tipo de gasto: {list[2]} \n Fecha de gasto: {list[3]} \n Cantidad de gasto: {list[4]} \n Observacion de gasto: {list[5]}"

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
        self.listSpent = OperateSpent().getAllSpent()
        for gasto in self.listSpent:
            self.tree.insert('', 'end',
                             values=(
                                 gasto.id, gasto.name,  OperateTypeSpent().getTypeSpentNameById(gasto.typeSpentId), gasto.date, gasto.amount,
                                 gasto.observation))

        # Ajustar las columnas
        for col in ('#1', '#2', '#3', '#4', '#5', '#6'):
            self.tree.column(col, anchor='center')
        scrollbar = ttk.Scrollbar(self.form, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        # Mostrar la tabla
        self.tree.grid(row=7, column=10, padx=25, pady=15)

    def getAllTypeSpent(self):
        self.listTypeSpent = OperateTypeSpent().getAllTypeSpent()
        listName = []
        for typeSpent in self.listTypeSpent:
            listName.append(typeSpent.typeSpent)
        return listName
    def initFormSpent(self):
        tk.Label(self.form, text="Nombre Gasto:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.form)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.form, text="Tipo Gasto:").grid(row=1, column=0)
        self.comboBoxType["values"] = self.getAllTypeSpent()
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
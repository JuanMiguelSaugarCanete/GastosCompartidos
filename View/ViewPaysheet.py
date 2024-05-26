import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
from tkinter import Frame

from Control.CtPaysheet import CtPaysheet


class ViewPaysheet:
    def __init__(self):
        self.form = tk.Tk()
        self.form.title("PANEL NOMINAS")
        self.form.geometry("1000x1000")
        self.monthsList = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE",
                           "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        self.amount = None
        self.comboBoxMonth = None
        self.comboBoxPerson = None
        self.tree = None
        self.comboBoxTypeOperation = None
        self.control = CtPaysheet()

    def addPay(self):
        amount = self.amount.get()
        month_name = self.comboBoxMonth.get()
        namePerson = self.comboBoxPerson.get()
        self.control.addPaysheet(amount,month_name,namePerson)
        self.updateTable()


    def updateTable(self):
        self.tree.delete(*self.tree.get_children())
        self.control.getDataListPaysheet(self.tree)

    def item_selected(self, event):
        selected_item = self.tree.focus()
        item = self.tree.item(selected_item)['values']
        operation = self.comboBoxTypeOperation.get()
        if(operation):
            self.control.deleteOrCopyItem(item[0],operation)
        self.updateTable()

    def leftSide(self):
        left_frame = Frame(self.form, width=900, height=400, background='#6B97E8')
        left_frame.grid(row=0, column=0, padx=50, pady=50)

        tk.Label(left_frame, text="Nomina:").grid(row=0, column=0, padx=10, pady=10)
        self.amount = tk.Entry(left_frame)
        self.amount.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(left_frame, text="Mes:").grid(row=1, column=0, padx=10, pady=10)
        self.comboBoxMonth = ttk.Combobox(left_frame, state="readonly")
        self.comboBoxMonth.grid(row=1, column=1, padx=10, pady=10)
        self.comboBoxMonth["values"] = self.monthsList

        tk.Label(left_frame, text="Persona:").grid(row=2, column=0, padx=10, pady=10)
        self.comboBoxPerson = ttk.Combobox(left_frame, state="readonly")
        self.comboBoxPerson.grid(row=2, column=1, padx=10, pady=10)

        self.comboBoxPerson["values"] = self.control.getDataListNamePerson()

        boton_enviar = tk.Button(left_frame, text="Añadir", command=self.addPay)
        boton_enviar.grid(row=3, column=0, columnspan=2)
    def rigthSide(self):
        rigth_frame = Frame(self.form, width=600, height=400, background='purple')
        rigth_frame.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(rigth_frame, text="Operacion:").grid(row=0, column=10, padx=25, pady=15)
        self.comboBoxTypeOperation = ttk.Combobox(rigth_frame, state="readonly")
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation["values"] = operationOption
        self.comboBoxTypeOperation.grid(row=1, column=10)

        self.tree = Treeview(rigth_frame, columns=('ID', 'Nombre Persona', 'Fecha', 'Cantidad'))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre Persona')
        self.tree.heading('#3', text='Fecha')
        self.tree.heading('#4', text='Cantidad')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.control.getDataListPaysheet(self.tree)
        self.tree.grid(row=2, column=10, padx=25, pady=15)

    def initForm(self):
        self.leftSide()
        self.rigthSide()
        self.form.mainloop()
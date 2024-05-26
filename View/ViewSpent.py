import tkinter as tk
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from tkinter import Frame
from datetime import datetime

from Control.CtSpent import CtSpent


class ViewSpent:

    def __init__(self):
        self.listTypeSpent = []
        self.listSpent = []
        self.form = tk.Tk()
        self.form.title("PANEL Gastos")
        self.form.geometry("1000x1000")
        self.control = CtSpent()
        self.initComponents()

    def initComponents(self):
        self.cal = None
        self.nombre = None
        self.typeSpent = None
        self.amount = None
        self.observation = None
        self.comboBoxType = None
        self.comboBoxTypeOperation = None
        self.tree = None

    def updateTable(self):
        self.tree.delete(*self.tree.get_children())
        self.control.getAllSpent(self.tree)

    def item_selected(self, event):
        selected_item = self.tree.focus()
        item = self.tree.item(selected_item)['values']
        operation = self.comboBoxTypeOperation.get()
        if(operation):
            self.control.copyOrDelete(item[0],operation)
        self.updateTable()
    def add(self):
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
        self.control.addSpent(name,typeSpent,dateNow,amount,observation)
        self.updateTable()
    def leftSide(self):
        left_frame = Frame(self.form, width=900, height=400, background='#6B97E8')
        left_frame.grid(row=0, column=0, padx=50, pady=50)

        tk.Label(left_frame, text="Nombre Gasto:").grid(row=0, column=0, padx=10, pady=10)
        self.nombre = tk.Entry(left_frame)
        self.nombre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(left_frame, text="Tipo Gasto:").grid(row=1, column=0, padx=10, pady=10)
        self.comboBoxType = ttk.Combobox(left_frame, state="readonly")
        self.comboBoxType["values"] = self.control.getAllTypeSpent()
        self.comboBoxType.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(left_frame, text="Fecha del gasto:").grid(row=2, column=0, padx=10, pady=10)
        self.cal = Calendar(left_frame)
        self.cal.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(left_frame, text="Cantidad:").grid(row=4, column=0, padx=10, pady=10)
        self.amount = tk.Entry(left_frame)
        self.amount.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(left_frame, text="Observaciones:").grid(row=5, column=0, padx=10, pady=10)
        self.observation = tk.Entry(left_frame)
        self.observation.grid(row=5, column=1, padx=10, pady=10)

        boton_enviar = tk.Button(left_frame, text="Añadir", command=self.add)
        boton_enviar.grid(row=6, column=0, columnspan=2)
    def rigthSide(self):
        rigth_frame = Frame(self.form, width=600, height=400, background='purple')
        rigth_frame.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(rigth_frame, text="Operacion:").grid(row=0, column=10, padx=25, pady=15)
        self.comboBoxTypeOperation = ttk.Combobox(rigth_frame, state="readonly")
        self.comboBoxTypeOperation.grid(row=1, column=10, padx=25, pady=15)
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation["values"] = operationOption

        self.tree = Treeview(rigth_frame, columns=('ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación'))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Tipo')
        self.tree.heading('#4', text='Fecha')
        self.tree.heading('#5', text='Cantidad')
        self.tree.heading('#6', text='Observación')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.control.getAllSpent(self.tree)
        self.tree.grid(row=2, column=10, padx=25, pady=15)

    def initForm(self):
        self.leftSide()
        self.rigthSide()
        self.form.mainloop()



from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview

from Data.OperatePaysheet import OperatePaysheet
from Data.OperatePerson import OperatePerson
from Model.Paysheet import Paysheet
from util.Util import Util


class CtPaysheet:
    def __init__(self):
        self.form = tk.Tk()
        self.form.title("PANEL NOMINAS")
        self.form.geometry("1000x1000")
        self.amount = tk.Entry(self.form)
        self.comboBoxMonth = ttk.Combobox(self.form, state="readonly")
        self.comboBoxPerson = ttk.Combobox(self.form, state="readonly")
        self.tree = Treeview(self.form, columns=('ID', 'Nombre Persona', 'Fecha', 'Cantidad'))
        self.comboBoxTypeOperation = ttk.Combobox(self.form, state="readonly")
        self.monthsNumber = {
            "ENERO": 1,
            "FEBRERO": 2,
            "MARZO": 3,
            "ABRIL": 4,
            "MAYO": 5,
            "JUNIO": 6,
            "JULIO": 7,
            "AGOSTO": 8,
            "SEPTIEMBRE": 9,
            "OCTUBRE": 10,
            "NOVIEMBRE": 11,
            "DICIEMBRE": 12

        }
    def getAllPerson(self):
        listName = []
        list = OperatePerson().getAllPerson()
        for person in list:
            listName.append(person.name)
        self.comboBoxPerson["values"] = listName
        tk.Label(self.form, text="Persona:").grid(row=2, column=0)
        self.comboBoxPerson.grid(row=2, column=1)
    def addPay(self):
        unique_id = Util().generateUniqueId()
        amount = self.amount.get()
        month_name = self.comboBoxMonth.get()
        namePerson = self.comboBoxPerson.get()
        month_number = self.getMonthNumberByName(month_name)
        idPerson = OperatePerson().personIdByName(namePerson)
        yearnow = datetime.now().year
        date = str(month_number) + "-" + str(yearnow)
        pay = Paysheet(unique_id,idPerson,amount,date)
        OperatePaysheet().addPaysheet(pay)

    def getAllPaysheet(self):
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation["values"] = operationOption
        tk.Label(self.form, text="Operacion:").grid(row=5, column=10)
        self.comboBoxTypeOperation.grid(row=6, column=10)

        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre Persona')
        self.tree.heading('#3', text='Fecha')
        self.tree.heading('#4', text='Cantidad')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        listAll = OperatePaysheet().getAllPaysheet()
        for paysheet in listAll:
            self.tree.insert('', 'end',
                             values=(paysheet.id,OperatePerson().personNameById(paysheet.personId),paysheet.date,paysheet.amount))
        for col in ('#1', '#2', '#3', '#4'):
            self.tree.column(col, anchor='center')
        self.tree.grid(row=7, column=10, padx=25, pady=15)

    def item_selected(self, event):
        print("sel")
    def getMonthNumberByName(self,name):
        if name in self.monthsNumber:
            return self.monthsNumber[name]
    def initForm(self):
        tk.Label(self.form, text="Nomina:").grid(row=0, column=0)
        self.amount = tk.Entry(self.form)
        self.amount.grid(row=0, column=1)
        month = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE",
                 "NOVIEMBRE", "DICIEMBRE"]
        self.comboBoxMonth["values"] = month
        tk.Label(self.form, text="Mes:").grid(row=1, column=0)
        self.comboBoxMonth.grid(row=1, column=1)
        self.getAllPerson()
        boton_enviar = tk.Button(self.form, text="Añadir", command=self.addPay)
        boton_enviar.grid(row=6, column=0, columnspan=2)
        self.getAllPaysheet()
        self.form.mainloop()
import tkinter as tk
import tkinter as tk
from tkinter import ttk

from Data.OperatePerson import OperatePerson

class CtPaysheet:
    def __init__(self):
        self.form = tk.Tk()
        self.amount = tk.Entry(self.form)
        self.comboBoxMonth = ttk.Combobox(self.form, state="readonly")
        self.comboBoxPerson = ttk.Combobox(self.form, state="readonly")

    def getAllPerson(self):
        listName = []
        list = OperatePerson().getAllPerson()
        for person in list:
            listName.append(person.name)
        self.comboBoxPerson["values"] = list
        tk.Label(self.form, text="Persona:").grid(row=2, column=0)
        self.comboBoxPerson.grid(row=2, column=1)

    def initForm(self):
        tk.Label(self.form, text="Nomina:").grid(row=0, column=0)
        self.amount = tk.Entry(self.form)
        self.amount.grid(row=0, column=1)
        month = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE",
                 "NOVIEMBRE", "DICIEMBRE"]
        self.comboBoxMonth["values"] = month
        tk.Label(self.form, text="Mes:").grid(row=1, column=0)
        self.comboBoxMonth.grid(row=1, column=1)
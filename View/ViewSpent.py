import tkinter as tk
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from tkinter import Frame
from datetime import datetime
import customtkinter

from Control.CtSpent import CtSpent
from util.Print import Print


class ViewSpent:

    def __init__(self):
        self.listTypeSpent = []
        self.listSpent = []
        self.form = None
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
        printComponent = Print()
        left_frame = customtkinter.CTkFrame(self.form, width=900, height=400)
        left_frame.grid(row=0, column=0, padx=50, pady=50)

        self.nombre = printComponent.entryWhithLabel(left_frame,"Nombre Gasto:",[0,0])

        self.comboBoxType = printComponent.getComboBoxWhithLabel(left_frame,"Tipo Gasto:",self.control.getAllTypeSpent(),[1,0])

        self.cal = printComponent.getCalendar(left_frame,[2,1])

        self.amount = printComponent.entryWhithLabel(left_frame,"Cantidad:",[4,0])

        self.observation =printComponent.entryWhithLabel(left_frame,"Observaciones:",[5,0])

        printComponent.btnSend(left_frame, "Añadir", self.add, [6, 0])

    def rigthSide(self):
        rigth_frame = customtkinter.CTkFrame(self.form, width=600, height=400)
        rigth_frame.grid(row=0, column=5, padx=5, pady=5)

        printComponent = Print()
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation = printComponent.getComboBoxWhithLabel(rigth_frame, "Operacion:", operationOption,[0, 10])
        col = ('ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación')
        self.tree = printComponent.getTable(rigth_frame,col,self.item_selected,[2,10])
        self.control.getAllSpent(self.tree)

    def initForm(self,right_Frame):
        self.form = right_Frame
        self.leftSide()
        self.rigthSide()



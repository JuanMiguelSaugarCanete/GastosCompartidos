import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview
from tkinter import Frame
import customtkinter

from Control.CtPaysheet import CtPaysheet
from util.Print import Print


class ViewPaysheet:
    def __init__(self):
        self.form = None
        #self.form.title("PANEL NOMINAS")
        #self.form.geometry("1000x1000")
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
        left_frame = customtkinter.CTkFrame(self.form)
        left_frame.grid(row=0, column=0, padx=50, pady=50)
        printComponent = Print()
        self.amount = printComponent.entryWhithLabel(left_frame,"Nomina:",[0,0])
        self.comboBoxMonth = printComponent.getComboBoxWhithLabel(left_frame,"Mes:",self.monthsList,[1,0])

        self.comboBoxPerson = printComponent.getComboBoxWhithLabel(left_frame,"Persona:",self.control.getDataListNamePerson(),[2,0])
        printComponent.btnSend(left_frame, "Añadir", self.addPay, [3, 0])
    def rigthSide(self):
        rigth_frame = customtkinter.CTkFrame(self.form)
        rigth_frame.grid(row=0, column=5, padx=5, pady=5)
        printComponent = Print()
        operationOption = ["ELIMINAR", "COPIAR"]
        self.comboBoxTypeOperation = printComponent.getComboBoxWhithLabel(rigth_frame,"Operacion:",operationOption,[0,10])
        col = ('ID', 'Nombre Persona', 'Fecha', 'Cantidad')
        self.tree = printComponent.getTable(rigth_frame,col,self.item_selected,[2,10])
        self.control.getDataListPaysheet(self.tree)

    def initForm(self,rigthLeft):
        self.form = rigthLeft
        self.leftSide()
        self.rigthSide()
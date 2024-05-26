from datetime import datetime
import tkinter as tk
from tkinter import Frame, messagebox
from tkinter import ttk
from tkinter.ttk import Treeview

from Data.OperatePaysheet import OperatePaysheet
from Data.OperatePerson import OperatePerson
from Model.Paysheet import Paysheet
from util.Util import Util


class CtPaysheet:
    def __init__(self):

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
    def addPaysheet(self,amount,month_name,namePerson):
        unique_id = Util().generateUniqueId()

        month_number = self.getMonthNumberByName(month_name)
        idPerson = OperatePerson().personIdByName(namePerson)
        yearnow = datetime.now().year
        date = str(month_number) + "-" + str(yearnow)
        pay = Paysheet(unique_id,idPerson,amount,date)
        OperatePaysheet().addPaysheet(pay)


    def deleteOrCopyItem(self, id,operation):
        if (operation == "ELIMINAR"):
            resultado = messagebox.askyesno("Confirmación", "¿Deseas continuar con la acción?")
            if resultado:
                OperatePaysheet().deletePaysheet(id)

        elif (operation == "COPIAR"):
            print(f"Elemento copiado")

    def getMonthNumberByName(self,name):
        if name in self.monthsNumber:
            return self.monthsNumber[name]

    def getDataListNamePerson(self):
        listName = []
        list = OperatePerson().getAllPerson()
        for person in list:
            listName.append(person.name)
        return listName

    def getDataListPaysheet(self,tree):
        listAll = OperatePaysheet().getAllPaysheet()
        for paysheet in listAll:
            tree.insert('', 'end',
                             values=(paysheet.id, OperatePerson().personNameById(paysheet.personId), paysheet.date,
                                     paysheet.amount))
        for col in ('#1', '#2', '#3', '#4'):
            tree.column(col, anchor='center')
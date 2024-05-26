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

    def addSpent(self,name,typeSpent,date,amount,observation):
        unique_id = Util().generateUniqueId()
        idTypeSpent = OperateTypeSpent().getTypeSpentIdByName(typeSpent)
        spent = Spent(unique_id,name,idTypeSpent,date,amount,observation)
        OperateSpent().addSpent(spent)

    def copyOrDelete(self, id,operation):

        if (operation == "ELIMINAR"):
            resultado = messagebox.askyesno("Confirmación", "¿Deseas continuar con la acción?")
            if resultado:
                OperateSpent().deleteSpent(id)

        elif (operation == "COPIAR"):
            print("Elemento copiado: ")

    def getAllSpent(self,tree):
        listSpent = OperateSpent().getAllSpent()
        for gasto in listSpent:
            tree.insert('', 'end',
                             values=(
                                 gasto.id, gasto.name,  OperateTypeSpent().getTypeSpentNameById(gasto.typeSpentId), gasto.date, gasto.amount,
                                 gasto.observation))

        # Ajustar las columnas
        for col in ('#1', '#2', '#3', '#4', '#5', '#6'):
            tree.column(col, anchor='center')

    def getAllTypeSpent(self):
        self.listTypeSpent = OperateTypeSpent().getAllTypeSpent()
        listName = []
        for typeSpent in self.listTypeSpent:
            listName.append(typeSpent.typeSpent)
        return listName

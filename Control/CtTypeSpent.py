import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Data.OperateTypeSpent import OperateTypeSpent
from Model.TipeSpent import TypeSpent
from util.ShowMenssage import ShowMensagge
from util.Util import Util


class CtTypeSpent:

    def __init__(self):
        self.formTypeSpent = tk.Tk()
        self.listTypeSpent = []
        self.nombre = tk.Entry(self.formTypeSpent)
        self.formTypeSpent.title("PANEL TIPOS GASTOS")
        self.formTypeSpent.geometry("1000x1000")
        self.comboBoxType = ttk.Combobox(self.formTypeSpent, state="readonly")
    def addTypeSpent(self):
        unique_id = Util().generateUniqueId()
        if (self.nombre.get()):
            typeSpent = TypeSpent(unique_id,self.nombre.get())
            OperateTypeSpent().addTypeSpent(typeSpent)
            self.updateCombo()
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_NOREGISTER_TITLE, Menssage.MSG_NOREGISTER_MSG)

    def deleteType(self):
        name = self.comboBoxType.get()
        for type in self.listTypeSpent:
            if(type.typeSpent == name):
                OperateTypeSpent().deleteType(type.id)
                self.updateCombo()
    def updateCombo(self):
        self.list= OperateTypeSpent().getAllTypeSpent()
        listName = []
        for type in self.listTypeSpent:
            listName.append(type.id)
        self.comboBoxType["values"] = listName
    def getAllTypeSpent(self):
        self.listTypeSpent = OperateTypeSpent().getAllTypeSpent()
        listName = []
        for typeSpent in self.listTypeSpent:
            listName.append(typeSpent.typeSpent)
        self.comboBoxType["values"] = listName
        self.comboBoxType.grid(row=0, column=2, padx=15, pady=15)
        buttonDelete = tk.Button(self.formTypeSpent, text="Eliminar", command=self.deleteType)
        buttonDelete.grid(row=0, column=4, columnspan=2)
    def initFormTypeSpent(self):

        tk.Label(self.formTypeSpent, text="Nuevo tipo gasto:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.formTypeSpent)
        self.nombre.grid(row=0, column=1)

        boton_enviar = tk.Button(self.formTypeSpent, text="Añadir", command=self.addTypeSpent)
        boton_enviar.grid(row=3, column=0, columnspan=2)
        self.getAllTypeSpent()
        self.formTypeSpent.mainloop()
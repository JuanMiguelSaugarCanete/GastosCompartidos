import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Control.CtTypeSpent import CtTypeSpent
from Data.OperateTypeSpent import OperateTypeSpent
from Model.TipeSpent import TypeSpent
from util.Print import Print
from util.ShowMenssage import ShowMensagge
from util.Util import Util
class ViewTypeSpent:
    def __init__(self):
        self.formTypeSpent =None
        self.listTypeSpent = []
        self.nombre = None
        self.comboBoxType = None
        self.control = CtTypeSpent()

    def add(self):
        name = str(self.nombre.get()).upper()
        self.control.addTypeSpent(name)
        self.updateCombo()
    def delete(self):
        name = self.comboBoxType.get()
        self.control.deleteType(name)
        self.updateCombo()

    def updateCombo(self):
        self.comboBoxType.configure(values=self.control.getAllTypeSpent())
    def initForm(self,right_Frame):
        self.formTypeSpent = right_Frame
        printComponent = Print()
        self.nombre = printComponent.entryWhithLabel(self.formTypeSpent, "Nuevo tipo gasto:", [0, 0])
        printComponent.btnSend(self.formTypeSpent, "Añadir", self.add, [0, 2])
        self.comboBoxType = printComponent.getComboBox(self.formTypeSpent,self.control.getAllTypeSpent(),[1,1])
        printComponent.btnDelete(self.formTypeSpent, "Eliminar", self.delete, [1, 2])
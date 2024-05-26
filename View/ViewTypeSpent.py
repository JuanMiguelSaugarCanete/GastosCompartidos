import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Control.CtTypeSpent import CtTypeSpent
from Data.OperateTypeSpent import OperateTypeSpent
from Model.TipeSpent import TypeSpent
from util.ShowMenssage import ShowMensagge
from util.Util import Util
class ViewTypeSpent:
    def __init__(self):
        self.formTypeSpent = tk.Tk()
        self.listTypeSpent = []
        self.nombre = tk.Entry(self.formTypeSpent)
        self.formTypeSpent.title("PANEL TIPOS GASTOS")
        self.formTypeSpent.geometry("1000x1000")
        self.comboBoxType = ttk.Combobox(self.formTypeSpent, state="readonly")
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
        self.comboBoxType["values"] = self.control.getAllTypeSpent()
    def initForm(self):
        tk.Label(self.formTypeSpent, text="Nuevo tipo gasto:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.formTypeSpent)
        self.nombre.grid(row=0, column=1)

        boton_enviar = tk.Button(self.formTypeSpent, text="Añadir", command=self.add)
        boton_enviar.grid(row=3, column=0, columnspan=2)

        self.comboBoxType["values"] = self.control.getAllTypeSpent()
        self.comboBoxType.grid(row=0, column=2, padx=15, pady=15)
        buttonDelete = tk.Button(self.formTypeSpent, text="Eliminar", command=self.delete)
        buttonDelete.grid(row=0, column=4, columnspan=2)
        self.formTypeSpent.mainloop()
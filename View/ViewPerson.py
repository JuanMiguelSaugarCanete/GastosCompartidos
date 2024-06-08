import tkinter as tk
from tkinter import ttk

from Control.CtPerson import CtPerson
from util.Print import Print


class ViewPerson:
    def __init__(self):
        self.formPerson = None
        self.listPerson = []
        self.nombre = None
        self.comboBoxPerson = None
        self.control = CtPerson()

    def updateCombo(self):
        self.comboBoxPerson.configure(values=self.control.getAllPerson())
    def add(self):
        name = self.nombre.get()
        self.control.addPerson(name)
        self.updateCombo()
    def delete(self):
        namePerson = self.comboBoxPerson.get()
        self.control.deletePerson(namePerson)
        self.updateCombo()
    def initForm(self,right_Frame):
        printComponent = Print()
        self.formPerson = right_Frame

        self.nombre = printComponent.entryWhithLabel(self.formPerson,"Nombre:",[0,0])
        printComponent.btnSend(self.formPerson,"Añadir",self.add,[0,2])

        self.comboBoxPerson = printComponent.getComboBox(self.formPerson,self.control.getAllPerson(),[1,1])
        printComponent.btnDelete(self.formPerson,"Eliminar", self.delete,[1,2])


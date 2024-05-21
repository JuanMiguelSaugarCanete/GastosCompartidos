import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Data.OperatePerson import OperatePerson
from Model.Person import Person
from util.ShowMenssage import ShowMensagge
from util.Util import Util


class CtPerson:

    def __init__(self):
        self.formPerson = tk.Tk()
        self.listPerson = []
        self.nombre = tk.Entry(self.formPerson)
        self.formPerson.title("PANEL PERSONAS")
        self.formPerson.geometry("1000x1000")
        self.comboBoxPerson = ttk.Combobox(self.formPerson, state="readonly")
    def addPerson(self):
        unique_id = Util().generateUniqueId()
        if(self.nombre.get()):
            person = Person(unique_id,self.nombre.get())
            OperatePerson().addPerson(person)
            self.updateCombo()
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_NOREGISTER_TITLE, Menssage.MSG_NOREGISTER_MSG)


    def deletePerson(self):
        namePerson = self.comboBoxPerson.get()
        for person in self.listPerson:
            if(person.name == namePerson):
                OperatePerson().deletePerson(person.id)
                self.updateCombo()

    def updateCombo(self):
        self.listPerson = OperatePerson().getAllPerson()
        listNamePerson = []
        for person in self.listPerson:
            listNamePerson.append(person.name)
        self.comboBoxPerson["values"] = listNamePerson
    def getAllPerson(self):
        self.listPerson = OperatePerson().getAllPerson()
        listNamePerson = []
        for person in self.listPerson:
            listNamePerson.append(person.name)
        self.comboBoxPerson["values"] = listNamePerson
        self.comboBoxPerson.grid(row=0, column=2,padx=15, pady=15)
        buttonDelete = tk.Button(self.formPerson, text="Eliminar", command=self.deletePerson)
        buttonDelete.grid(row=0, column=4, columnspan=2)

    def initFormPerson(self):

        tk.Label(self.formPerson, text="Nombre:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.formPerson)
        self.nombre.grid(row=0, column=1)

        boton_enviar = tk.Button(self.formPerson, text="Añadir", command=self.addPerson)
        boton_enviar.grid(row=3, column=0, columnspan=2)
        self.getAllPerson()

        self.formPerson.mainloop()
import tkinter as tk
from tkinter import ttk

from Control.CtPerson import CtPerson


class ViewPerson:
    def __init__(self):
        self.formPerson = tk.Tk()
        self.listPerson = []
        self.nombre = tk.Entry(self.formPerson)
        self.formPerson.title("PANEL PERSONAS")
        self.formPerson.geometry("1000x1000")
        self.comboBoxPerson = ttk.Combobox(self.formPerson, state="readonly")
        self.control = CtPerson()

    def updateCombo(self):
        self.comboBoxPerson["values"] = self.control.getAllPerson()

    def add(self):
        name = self.nombre.get()
        self.control.addPerson(name)
        self.updateCombo()
    def delete(self):
        namePerson = self.comboBoxPerson.get()
        self.control.deletePerson(namePerson)
        self.updateCombo()
    def initForm(self):
        tk.Label(self.formPerson, text="Nombre:").grid(row=0, column=0)
        self.nombre = tk.Entry(self.formPerson)
        self.nombre.grid(row=0, column=1)

        boton_enviar = tk.Button(self.formPerson, text="Añadir", command=self.add)
        boton_enviar.grid(row=3, column=0, columnspan=2)

        self.comboBoxPerson["values"] = self.control.getAllPerson()
        self.comboBoxPerson.grid(row=0, column=2, padx=15, pady=15)
        buttonDelete = tk.Button(self.formPerson, text="Eliminar", command=self.delete)
        buttonDelete.grid(row=0, column=4, columnspan=2)
        self.formPerson.mainloop()
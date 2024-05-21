from tkinter import ttk
from tkinter.ttk import Treeview

from tkcalendar import Calendar
import tkinter as tk


"""
print = Print(self.form)
        listElement = [
            {
                "type":print.ENTRY,
                "order":0,
                "txtLabel":"Nombre Gasto:",
                "var":self.nombre
            },
            {
                "type":print.COMBOBOX,
                "order":1,
                "txtLabel":"Tipo Gasto:",
                "var":self.listTypeSpent,
                "values": self.getAllTypeSpent()
            },
            {
                "type": print.CALENDAR,
                "order": 2,
                "txtLabel": "Fecha del gasto:",
                "var": self.cal
            },

            {
                "type":print.ENTRY,
                "order":3,
                "txtLabel":"Cantidad:",
                "var":self.amount
            },
            {
                "type": print.ENTRY,
                "order": 4,
                "txtLabel": "Observaciones:",
                "var": self.observation
            },
            {
                "type": print.BUTTON,
                "order": 5,
                "txtLabel": "Añadir:",
                "command": self.addSpent,
                "columnspan":2
            },
            {
                "type": print.COMBOBOX,
                "order": 1,
                "txtLabel": "Operacion:",
                "coordenates":[9,10],
                "var": self.comboBoxTypeOperation,
                "values": ["ELIMINAR", "COPIAR"]
            },
            {
                "type": print.TABLE,
                "order": 6,
                "var": self.tree,
                "head": ['ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación'],
                "bind": ['<<TreeviewSelect>>', self.item_selected],
                "values": self.prueba()
            }
        ]
        print.printElements(listElement)
        """
class Print:

    def __init__(self,form):
        self.form = form
        self.position = 0
        self.ENTRY = "ENTRY"
        self.COMBOBOX = "COMBOBOX"
        self.TABLE = "TABLE"
        self.CALENDAR = "CALENDAR"
        self.BUTTON = "BUTTON"
    def printElements(self,list):
        lenOfElements = len(list)
        self.position = 0
        #for contElement in range(lenOfElements):
        for dataList in list:
            type = dataList["type"]
            if(self.ENTRY == type):
                txtLabel = dataList["txtLabel"]
                var = dataList["var"]
                tk.Label(self.form, text=f"{txtLabel}").grid(row=self.position, column=0)
                var = tk.Entry(self.form)
                var.grid(row=self.position, column=1)
                self.position +=1
            elif(self.COMBOBOX == type):
                txtLabel = dataList["txtLabel"]
                var = dataList["var"]
                values = dataList["values"]
                var = ttk.Combobox(self.form, state="readonly")
                var["values"] = values
                if "coordenates" in dataList:
                    row = dataList["coordenates"][0]
                    col = dataList["coordenates"][1]
                    tk.Label(self.form, text=txtLabel).grid(row=row, column=col)
                    row +=1
                    var.grid(row=row, column=col)
                else:
                    tk.Label(self.form, text=txtLabel).grid(row=self.position, column=0)
                    var.grid(row=self.position, column=1)
                self.position +=1
            elif(self.TABLE == type):
                var = dataList["var"]
                head = dataList["head"]
                var = Treeview(self.form, columns=('ID', 'Nombre', 'Tipo', 'Fecha', 'Cantidad', 'Observación'))
                headCont = 1
                for headData in head:
                    var.heading(f'#{headCont}',text=headData)
                    headCont +=1
                var.bind(dataList["bind"][0],dataList["bind"][1])
                values = dataList["values"]
                for dataValue in values:
                    var.insert('', 'end',values=(dataValue[0], dataValue[1],dataValue[2],dataValue[3], dataValue[4],dataValue[5]))
                for col in range(len(head)):
                    var.column(col, anchor='center')
                var.grid(row=12, column=10, padx=25, pady=15)
                self.position +=1
            elif(self.CALENDAR == type):
                txtLabel = dataList["txtLabel"]
                var = dataList["var"]
                tk.Label(self.form, text=txtLabel).grid(row=self.position, column=0)
                var = Calendar(self.form)
                var.grid(row=self.position, column=1)
                self.position +=4
            elif(self.BUTTON == type):
                txtLabel = dataList["txtLabel"]
                command = dataList["command"]
                tk.Button(self.form, text=txtLabel, command=command).grid(row=self.position, column=0, columnspan=2)
                self.position +=1


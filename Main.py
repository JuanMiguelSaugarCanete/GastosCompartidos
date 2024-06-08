import json
import os
import tkinter as tk
from configparser import ConfigParser
from tkinter import filedialog

import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Configuration.Configuration import Configuration
from Model.TipeSpent import TypeSpent
from View.ViewPaysheet import ViewPaysheet
from View.ViewPerson import ViewPerson
from View.ViewTypeSpent import ViewTypeSpent
from View.ViewSpent import ViewSpent
from util.Print import Print
from util.ShowMenssage import ShowMensagge
from util.Util import Util
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Frame

right_Frame = None
main = None
config = ConfigParser()
config.read("Configuration/configuration.conf")
configuration = Configuration()
for section in config.sections():
    for item in config.items(section):
        configuration.configuration.update({f"{item[0]}":item[1]})

p = configuration.configuration["filebbdd"]
existBbdd = False
if( p):
    print("esta el valor : "+configuration.configuration["filebbdd"])
    existBbdd = True
else:
    print("Nada")

def destroyRightSide():
    for widget in right_Frame.winfo_children():
        widget.destroy()
def openSpent():
    control = ViewSpent()
    destroyRightSide()
    control.initForm(right_Frame)
def openTypeSpent():
    control = ViewTypeSpent()
    destroyRightSide()
    control.initForm(right_Frame)
def openPerson():
    control=ViewPerson()
    destroyRightSide()
    control.initForm(right_Frame)

def openPaysheet():
    control=ViewPaysheet()
    destroyRightSide()
    control.initForm(right_Frame)


def datos(ax):
    prueba = ['Prueba1', 240]
    pruebaDos = ['Prueba2', 500]
    pruebaTres = ['Prueba3', 240]
    pruebaCuatro = ['Prueba4', 240]

    lista = [prueba, pruebaDos, pruebaTres, pruebaCuatro]
    df_lista = pd.DataFrame(lista, columns=['Nombre', 'Cantidad'])
    ax.pie(df_lista['Cantidad'], labels=df_lista['Nombre'])

if(existBbdd):
    main = tk.Tk()
    main.configure(background='#6B97E8')
    main.title("PANEL PRINCIPAL")
    main.geometry("1000x1000")
    main.grid_columnconfigure(1, weight=0)
    main.grid_columnconfigure((2, 3), weight=0)
    main.grid_rowconfigure((0, 1, 2), weight=1)
    print = Print()
    btn_Frame = customtkinter.CTkFrame(main)
    btn_Frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    print.btn_main(btn_Frame,"Panel Gastos",openSpent,[0,0])
    print.btn_main(btn_Frame, "Panel Personas", openPerson, [1, 0])
    print.btn_main(btn_Frame, "Panel Tipo Gastos", openTypeSpent, [2, 0])
    print.btn_main(btn_Frame, "Panel Nominas", openPaysheet, [3, 0])
    print.btn_main(btn_Frame, "Configuracion", openPaysheet, [4, 0])

    right_Frame = customtkinter.CTkFrame(main)

    right_Frame.grid(row=0, column=5, padx=5, pady=5)

    fig, ax = plt.subplots()
    datos(ax)
    canvas = FigureCanvasTkAgg(fig,master=right_Frame)
    canvas.get_tk_widget().grid(row=0, column=5, padx=5, pady=5)



    main.mainloop()
else:
    def obtenerRuta():
        filename = filedialog.askdirectory(initialdir="/", title="Selecciona el archivo")
        ruta.set(filename)
        print(f"Ruta del directorio: {filename}")
    def crearBBDD():
        if(ruta.get()):
            typeSpent = ["ALQUILER","COMPRA","INTERNET","STREAMING","AGUA","LUZ","COMBUSTIBLE"]
            listType = []
            for type in typeSpent:
                unique_id = Util().generateUniqueId()
                typeSpent = TypeSpent(unique_id, type)
                listType.append(typeSpent.toJSON())
            bbdd = {"GASTOS": [{"PERSON": [], "SPENT": [], "TYPESPENT": [], "PAYSHEET": []}]}
            print(bbdd)
            with open(f'{ruta.get()}\db.json', 'x') as archivo:
                archivo.write("")
            with open(f'{ruta.get()}\db.json', 'r+') as archivo:
                archivo.seek(0)
                json.dump(bbdd, archivo)
            for type in listType:
                with open(f'{ruta.get()}\db.json', 'r+') as file:
                    file_data = json.load(file)
                    file_dataColection = file_data['GASTOS'][0]['TYPESPENT']
                    file_dataColection.append(type)
                    file.seek(0)
                    json.dump(file_data, file)
            config.set('GENERAL','filebbdd',f'{ruta.get()}/db.json')
            with open('Configuration/configuration.conf', 'w') as archivo:
                config.write(archivo)



        else:
            print("No hay ruta")
            ShowMensagge().warningMensagge("No hay ruta", "Debe de seleccionar una ruta para crear la base de datos")


    root = tk.Tk()
    root.title("Bienvenido")
    root.geometry("300x300")
    ruta = tk.StringVar()
    upper = tk.Frame(root, width=900, height=400, background='#6B97E8')
    upper.grid(row=0, column=0, padx=50, pady=50)
    down = tk.Frame(root, width=900, height=400, background='#6B97E8')
    down.grid(row=1, column=0, padx=50, pady=50)
    tk.Label(upper, text="Bienvenido! para empezar deberas elegir la ruta donde lo quieras guardar tu base de datos:").grid(row=0,column=0, padx=10, pady=10)
    boton = tk.Button(down, text="Abrir archivo", command=obtenerRuta)
    boton.grid(row=0,column=0, padx=10, pady=10)

    label_ruta = tk.Entry(down, textvariable=ruta, state="readonly")
    label_ruta.grid(row=0,column=1, padx=10, pady=10)

    boton = tk.Button(down, text="crear", command=crearBBDD)
    boton.grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()
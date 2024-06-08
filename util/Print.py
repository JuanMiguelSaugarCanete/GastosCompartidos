import tkinter

import customtkinter
import customtkinter as ctk
from tkinter.ttk import Treeview
from tkcalendar import Calendar
import tkinter as tk
class Print:

    def btn_main(self,frame,text,command,position):
        button = customtkinter.CTkButton(frame,text=text,command=command, font=customtkinter.CTkFont(size=20, weight="bold"))
        button.grid(row=position[0], column=position[1], padx=20, pady=10)

    def btnSend(self,frame,text,command,position):
        button = customtkinter.CTkButton(frame,text=text,command=command, font=customtkinter.CTkFont(size=10, weight="bold"))
        button.grid(row=position[0], column=position[1], padx=20, pady=10, columnspan=2)
    def btnDelete(self,frame,text,command,position):
        button = customtkinter.CTkButton(frame,text=text,command=command, font=customtkinter.CTkFont(size=10, weight="bold"),fg_color="#DE4E5A")
        button.grid(row=position[0], column=position[1], padx=20, pady=10, columnspan=2)
        button.configure(hover_color="#E15648")

    def entryWhithLabel(self,frame,txtLabel,position):
        label = customtkinter.CTkLabel(frame,text=txtLabel)
        label.grid(row=position[0], column=position[1], padx=20, pady=10)
        entry = customtkinter.CTkEntry(frame)
        entry.grid(row=position[0], column=position[1]+1, padx=20, pady=10)
        return entry

    def getComboBox(self,frame,values,position):
        combobox = customtkinter.CTkComboBox(frame,state="readonly",values=values)
        combobox.grid(row=position[0], column=position[1], padx=15, pady=15)
        return combobox
    def getComboBoxWhithLabel(self,frame,txtLabel,values,position):
        label = customtkinter.CTkLabel(frame, text=txtLabel)
        label.grid(row=position[0], column=position[1], padx=20, pady=10)
        combobox = customtkinter.CTkComboBox(frame,state="readonly",values=values)
        combobox.grid(row=position[0], column=position[1]+1, padx=15, pady=15)
        return combobox
    def getTable(self,frame,columns,command,position):
        tree = Treeview(frame,columns=columns)
        contHeading = 1
        for column in columns:
            tree.heading(f'#{contHeading}', text=column)
            contHeading += 1
        tree.bind('<<TreeviewSelect>>', command)
        tree.grid(row=position[0], column=position[1], padx=25, pady=15)
        return tree
    def getCalendar(self,frame,position):
        calendar = Calendar(frame)
        calendar.grid(row=position[0], column=position[1], padx=10, pady=10)
        return calendar

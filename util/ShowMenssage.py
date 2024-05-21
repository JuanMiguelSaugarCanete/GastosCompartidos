from tkinter import messagebox

from Configuration import Menssage


class ShowMensagge:
    def warningMensagge(self,title,menssage):
        messagebox.showwarning(title, menssage)
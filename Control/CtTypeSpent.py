import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Data.OperateTypeSpent import OperateTypeSpent
from Model.TipeSpent import TypeSpent
from util.ShowMenssage import ShowMensagge
from util.Util import Util


class CtTypeSpent:

    def addTypeSpent(self,name):
        unique_id = Util().generateUniqueId()
        if (name):
            typeSpent = TypeSpent(unique_id,name)
            OperateTypeSpent().addTypeSpent(typeSpent)
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_NOREGISTER_TITLE, Menssage.MSG_NOREGISTER_MSG)

    def deleteType(self,name):
        listTypeSpent = OperateTypeSpent().getAllTypeSpent()
        for type in listTypeSpent:
            if(type.typeSpent == name):
                OperateTypeSpent().deleteType(type.id)
    def getAllTypeSpent(self):
        listTypeSpent = OperateTypeSpent().getAllTypeSpent()
        listName = []
        for typeSpent in listTypeSpent:
            listName.append(typeSpent.typeSpent)
        return listName


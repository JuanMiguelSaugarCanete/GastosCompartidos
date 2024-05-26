import tkinter as tk
from tkinter import ttk

from Configuration import Menssage
from Data.OperatePerson import OperatePerson
from Model.Person import Person
from util.ShowMenssage import ShowMensagge
from util.Util import Util


class CtPerson:

    def addPerson(self,name):
        unique_id = Util().generateUniqueId()
        if(name):
            person = Person(unique_id,name)
            OperatePerson().addPerson(person)
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_NOREGISTER_TITLE, Menssage.MSG_NOREGISTER_MSG)

    def deletePerson(self,namePerson):
        listPerson = OperatePerson().getAllPerson()
        for person in listPerson:
            if(person.name == namePerson):
                OperatePerson().deletePerson(person.id)
    def getAllPerson(self):
        listPerson = OperatePerson().getAllPerson()
        listNamePerson = []
        for person in listPerson:
            listNamePerson.append(person.name)
        return listNamePerson




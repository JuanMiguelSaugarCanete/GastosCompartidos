from tkinter import messagebox

from Configuration import Menssage
from Data.OperateGeneral import OperateGeneral
from Model.Person import Person

from util.ShowMenssage import ShowMensagge


class OperatePerson(OperateGeneral):


    def __init__(self):
        self.collectionName = 'PERSON'
    def addPerson(self,person):
        file_dataPerson = self.readColection(self.collectionName)
        if (len(file_dataPerson) < 2):
            self.updateColection(self.collectionName,person.toJSON())
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_LIMITPERSON_TITLE, Menssage.MSG_LIMITPERSON_MSG)
    def getAllPerson(self):
        list = []
        file_dataPerson = self.readColection(self.collectionName)
        if(len(file_dataPerson) > 0):
            for data in file_dataPerson:
                person = Person(data.get("id"), data.get("name"))
                list.append(person)
        return list

    def deletePerson(self,id):
        self.deleteRegisterCollectionById(self.collectionName,id)


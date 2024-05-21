from Configuration import Menssage
from Data.OperateGeneral import OperateGeneral
from Model.TipeSpent import TypeSpent
from util.ShowMenssage import ShowMensagge


class OperateTypeSpent(OperateGeneral):
    def __init__(self):
        self.collectionName = 'TYPESPENT'

    def addTypeSpent(self,typeSpent):
        existName = False
        file_dataTypeSpent = self.readColection(self.collectionName)
        for data in file_dataTypeSpent:
            if(str(data.get("name")).upper() == str(typeSpent.typeSpent).upper()):
                existName = True
        if(existName == False):
            self.updateColection(self.collectionName,typeSpent.toJSON())
        else:
            ShowMensagge().warningMensagge(Menssage.MSG_LIMITPERSON_TITLE, Menssage.MSG_LIMITPERSON_MSG)

    def getAllTypeSpent(self):
        list = []
        file_dataTypeSpent = self.readColection(self.collectionName)
        if(len(file_dataTypeSpent) > 0):
            for data in file_dataTypeSpent:
                typeSpent = TypeSpent(data.get("id"), data.get("typeSpent"))
                list.append(typeSpent)
        return list
    def getTypeSpentNameById(self,id):
        name = None
        file_dataTypeSpent = self.readColection(self.collectionName)
        if(len(file_dataTypeSpent) > 0):
            for data in file_dataTypeSpent:
                if(data.get("id") == id):
                    name = data.get("typeSpent")
        return name
    def getTypeSpentIdByName(self,name):
        id = None
        file_dataTypeSpent = self.readColection(self.collectionName)
        if(len(file_dataTypeSpent) > 0):
            for data in file_dataTypeSpent:
                if(data.get("typeSpent") == name):
                    id = data.get("id")
        return id
    def deleteType(self,id):
        self.deleteRegisterCollectionById(self.collectionName,id)
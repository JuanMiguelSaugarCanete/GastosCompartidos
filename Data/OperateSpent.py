from Data.OperateGeneral import OperateGeneral
from Model.Spent import Spent


class OperateSpent(OperateGeneral):
    def __init__(self):
        self.collectionName = 'SPENT'
    def addSpent(self,spent):
        self.updateColection(self.collectionName, spent.toJSON())
    def getAllSpent(self):
        list = []
        file_dataSpent = self.readColection(self.collectionName)
        if(len(file_dataSpent) > 0):
            for data in file_dataSpent:
                spent = Spent(data.get("id"),
                                  data.get("name"),
                                  data.get("typeSpentId"),
                                  data.get("date"),
                                  data.get("amount"),
                                  data.get("observation"))
                list.append(spent)
        return list
    def deleteType(self,id):
        self.deleteRegisterCollectionById(self.collectionName,id)
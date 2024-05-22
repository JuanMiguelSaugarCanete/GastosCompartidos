from Data.OperateGeneral import OperateGeneral
from Model.Paysheet import Paysheet


class OperatePaysheet(OperateGeneral):
    def __init__(self):
        self.collectionName = 'PAYSHEET'

    def addPaysheet(self,paysheet):
        self.updateColection(self.collectionName,paysheet.toJSON())

    def getAllPaysheet(self):
        file_data = self.readColection(self.collectionName)
        list = []
        if (len(file_data) > 0):
            for data in file_data:
                paysheet = Paysheet(data.get("id"),data.get("personId"),data.get("amount"),data.get("date"))
                list.append(paysheet)
        return list


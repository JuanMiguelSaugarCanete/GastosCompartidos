import json


class OperateGeneral:
    dataBase = 'D:/DESARROLLO/REPOSITORY/GASTOSCOMPARTIDOS/bbdd/db.json'
    def readColection(self,collection):
        with open(self.dataBase, 'r') as file:
            file_data = json.load(file)
            return  file_data['GASTOS'][0][collection]

    def updateColection(self,collection,dicctionary):
        with open(self.dataBase, 'r+') as file:
            file_data = json.load(file)
            file_dataPerson = file_data['GASTOS'][0][collection]
            file_dataPerson.append(dicctionary)
            file.seek(0)
            json.dump(file_data, file)

    def deleteRegisterCollectionById(self,collection,id):
        oldData = None
        with open(self.dataBase, 'r') as file:
            oldData = json.load(file)

        file_data = oldData['GASTOS'][0][collection]
        for dataRegister in file_data:
            if (dataRegister.get("id") == id):
                oldData['GASTOS'][0][collection].remove(dataRegister)

        with open(self.dataBase, 'w') as file:
            json.dump(oldData, file)
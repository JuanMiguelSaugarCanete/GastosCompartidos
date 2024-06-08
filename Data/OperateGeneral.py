import json
from Configuration.Configuration import Configuration

class OperateGeneral:

    def readColection(self,collection):
        configuration = Configuration()
        self.dataBase = configuration.configuration["filebbdd"]
        if(self.dataBase):
            with open(self.dataBase, 'r') as file:
                file_data = json.load(file)
                return file_data['GASTOS'][0][collection]



    def updateColection(self,collection,dicctionary):
        configuration = Configuration()
        self.dataBase = configuration.configuration["filebbdd"]
        with open(self.dataBase, 'r+') as file:
            file_data = json.load(file)
            file_dataPerson = file_data['GASTOS'][0][collection]
            file_dataPerson.append(dicctionary)
            file.seek(0)
            json.dump(file_data, file)

    def deleteRegisterCollectionById(self,collection,id):
        configuration = Configuration()
        self.dataBase = configuration.configuration["filebbdd"]
        oldData = None
        with open(self.dataBase, 'r') as file:
            oldData = json.load(file)

        file_data = oldData['GASTOS'][0][collection]
        for dataRegister in file_data:
            if (dataRegister.get("id") == id):
                oldData['GASTOS'][0][collection].remove(dataRegister)

        with open(self.dataBase, 'w') as file:
            json.dump(oldData, file)
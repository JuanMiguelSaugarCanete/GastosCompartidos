class Spent:
    def __init__(self,id, name,typeSpentId,date,amount,observation):
        self.id = id
        self.name = name
        self.typeSpentId = typeSpentId
        self.date = date
        self.amount = amount
        self.observation = observation

    def toJSON(self):
        return {"id": self.id,"name": self.name,"typeSpentId": self.typeSpentId,"date": self.date,"amount": self.amount,"observation": self.observation}

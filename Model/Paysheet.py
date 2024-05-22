class Paysheet:
    def __init__(self,id,personId,amount,date):
        self.id = id
        self.personId = personId
        self.amount = amount
        self.date = date
    def toJSON(self):
        return {"id": self.id,"personId": self.personId,"amount": self.amount,"date": self.date}
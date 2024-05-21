class Paysheet:
    def __init__(self,id,personid,amount,date):
        self.id = id
        self.personid = personid
        self.amount = amount
        self.date = date
    def toJSON(self):
        return {"id": self.id,"personid": self.personid,"amount": self.amount,"date": self.date}
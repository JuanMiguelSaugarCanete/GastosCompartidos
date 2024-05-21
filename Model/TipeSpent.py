class TypeSpent:
    def __init__(self, id,typeSpent):
        self.id = id
        self.typeSpent = typeSpent
    def toJSON(self):
        return {"id": self.id,"typeSpent": self.typeSpent}
class Room(): 

    def __init__(self, id, OG, number_1, number_2): 

        self.setID(id) 
        self.setOG(OG)
        self.setNumber_1(number_1)
        self.setNumber_2(number_2)

    def setID(self, id): 
        self.id = id

    def getID(self): 
        return self.id
    
    def setOG(self, OG): 
        self.OG = OG

    def getOG(self): 
        return self.OG
    
    def setNumber_1(self, number_1): 
        self.number_1 = number_1

    def getNumber_1(self): 
        return self.number_1
    
    def setNumber_2(self, number_2): 
        self.number_2 = number_2

    def getNumber_2(self): 
        return self.number_2
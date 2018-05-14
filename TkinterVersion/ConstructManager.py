import Construct

class ConstructManager():

    def __init__(self):

        self.construct1 = Construct.Construct("<")
        self.constructList = [self.construct1]

    def addConstruct(self, construct):
        print("Added construct to construct list")

    def getConstruct(self, name):
        print("Getting contsruct from construct list")

    def deleteConstruct(self, name):
        print("Deleting construct from construct list")
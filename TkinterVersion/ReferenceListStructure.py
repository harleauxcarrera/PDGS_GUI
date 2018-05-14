class ReferenceList():

    def __init__(self):

        self.referenceList = ["Reference 1", "Reference 2", "Reference 3"]

    def addReference(self, reference):

        print("Added a reference to the reference list")

    def deleteReference(self, name):

        print("Deleted reference from reference list")

    def getReference(self, index):

        return self.referenceList[index]
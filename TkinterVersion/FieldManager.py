import Field

class FieldManager():

    def __init__(self):

        self.field1 = Field.Field("Name", "ABB", "DES", "REF", "DATATYPE", "BASE", "MASK", "VALUECON", "1")
        self.FieldList = [self.field1]

    def addField(self, field):

        print("Added a field to the field list")

    def getField(self, name):

        print("Getting field from field list")

    def deleteField(self, name):

        print("Deleting field from field list")
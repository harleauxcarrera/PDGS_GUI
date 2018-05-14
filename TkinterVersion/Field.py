import ReferenceListStructure

class Field():

    def __init__(self, name, abb, des, reference, datatype, base, mask, valuecon, require):

        self.Name = name
        self.Abbreviation = abb
        self.Description = des
        self.Reference = reference
        self.DataType = datatype
        self.Base = base
        self.Mask = mask
        self.ValueConstraint = valuecon
        self.Require = require
        self.ReferenceList = ReferenceListStructure.ReferenceList()

    def setName(self, name):
        self.Name = name

    def getName(self):
        return self.Name

    def setAbb(self, abb):
        self.Abbreviation = abb

    def getAbb(self):
        return self.Abbreviation

    def setDes(self, des):
        self.Description = des

    def getDes(self):
        return self.Description

    def setReference(self,reference):
        self.Reference = reference

    def getReference(self):
        return self.Reference

    def setDataType(self, datatype):
        self.DataType = datatype

    def getDataType(self):
        return self.DataType

    def setBase(self, base):
        self.Base = base

    def getBase(self):
        return self.Base

    def setMask(self, mask):
        self.Mask = mask

    def getMask(self):
        return self.Mask

    def setValCon(self, valcon):
        self.ValueConstraint = valcon

    def getValCon(self):
        return self.ValueConstraint

    def setRequired(self, require):
        self.Require = require

    def getRequired(self):
        return self.Require
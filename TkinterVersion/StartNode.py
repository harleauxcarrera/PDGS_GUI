class StartNode():

    def __init__(self, protoname, protodes, depprotoname, deppattern):

        self.ProtocolName = protoname
        self.ProtocolDescription = protodes
        self.DependentProtocolName = depprotoname
        self.DependencyPattern = deppattern

    def setProtoName(self, protoname):
        self.ProtocolName = protoname

    def getProtoName(self):
        return self.ProtocolName
    def setProtoDes(self, protodes):
        self.ProtocolDescription = protodes
    def getProtoDes(self):
        return self.ProtocolDescription
    def setDepProtoName(self, depprotoname):
        self.DependentProtocolName = depprotoname
    def getDepProtoName(self):
        return self.DependentProtocolName
    def setDepPattern(self, deppattern):
        self.DependencyPattern  = deppattern
    def getDepPatter(self):
        return self.DependencyPattern
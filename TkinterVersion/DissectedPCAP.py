#import DissectorScript
#import Tshark

class DissectedPCAP():

    def __init__(self):

        self.readableInformation = 0
        self.packetArray = 0
        self.Tshark = 0

    def applyToPCAP(self, pdtScript):

        if(pdtScript != 0):
            self.readableInformation = self.Tshark.apply(pdtScript)

    def getDissectedPCAP(self):
        return self.readableInformation

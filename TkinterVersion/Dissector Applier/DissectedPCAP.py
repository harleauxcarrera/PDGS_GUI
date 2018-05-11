#import DissectorScript
#import Tshark

class DissectedPCAP:
    readableInformation = 0
    self.applyToPCAP(pdtScript)
    packetArray = 0

    def applyToPCAP(self, pdtScript):
        if(pdtScript != null) {
            self.readableInformation = Tshark.apply(pdtScript)
        }

    def getDissectedPCAP(self):
        return self.readableInformation

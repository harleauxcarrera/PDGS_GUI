import ProtocolDecisionTree
import DissectedPCAP
import PCAP

class DissectorScript():

    def __init__(self):

        self.ProtocolDecisionTree = ProtocolDecisionTree.ProtocolDecisionTree()
        self.dissectedPCAP = DissectedPCAP.DissectedPCAP()
        self.PCAP = PCAP.PCAP()

    def generateDissectorScript(self):
        print("Generating Dissector Script")

    def getDissectorScript(self):
        print("Getting Dissector Script")

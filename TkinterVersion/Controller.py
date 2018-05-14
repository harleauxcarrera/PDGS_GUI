#import PCAP
#import DissectedPCAP
#import DissectorScript
#import WorkspaceManager
import Workspace


class Controller():

    def __init__(self):

        self.PCAP = 0
        self.DissectedPCAP = 0
        self.DissectorScript = 0
        self.WorkspaceManager = 0
        self.workspace = Workspace.Workspace("Workspace1")

    def generateXMLFormat(self):

        self.workspace.saveProjectAsXML()
        print("XML File Generated")

    def generateLUAFormat(self):

        print("LUA File Generated")



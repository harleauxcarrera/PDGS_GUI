import DissectorScript
import WorkspaceManager
import ProtocolDecisionTree


class Controller():

    def __init__(self):

        self.DissectorScript = DissectorScript.DissectorScript()
        self.WorkspaceManager = WorkspaceManager.WorkspaceManager()
        self.ProtocolDecisionTree = ProtocolDecisionTree.ProtocolDecisionTree()

    def generateXMLFormat(self):

        self.WorkspaceManager.workspace1.saveProjectAsXML()
        print("XML File Generated")

    def generateLUAFormat(self):

        print("LUA File Generated")



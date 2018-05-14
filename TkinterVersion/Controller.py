import DissectorScript
import WorkspaceManager
import ProtocolDecisionTree
import Workspace


class Controller():

    def __init__(self):

        self.DissectorScript = DissectorScript.DissectorScript()
        self.WorkspaceManager = WorkspaceManager.WorkspaceManager()
        self.ProtocolDecisionTree = ProtocolDecisionTree.ProtocolDecisionTree()
        self.workspace = Workspace.Workspace("Workspace1")

    def generateXMLFormat(self):

        self.WorkspaceManager.workspace1.saveProjectAsXML()
        print("XML File Generated")

    def generateLUAFormat(self):

        print("LUA File Generated")



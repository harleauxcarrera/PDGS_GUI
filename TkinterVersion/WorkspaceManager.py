import Workspace

class WorkspaceManager():

    def __init__(self):
        self.activeWorkspace = "Workspace1"
        self.workspace1 = Workspace.Workspace("workspace1")
        self.workspaceList = [self.workspace1]

    #def setActiveWorksace(self):
    #def getActiveWorkspace(self):
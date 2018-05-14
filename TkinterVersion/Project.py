class Project():

    projectName = "Project1"
    projectDescription = "This is a project"
    numberOfProjects = 0
    #protocolDecisionTree = PDT
    #dissector = DissectorScript


    def __init__(self, projectName, projectDescription):
        self.projectName = projectName
        self.projectDescription = projectDescription
        Project.numberOfProjects += 1

    def getProjectName(self):
        return self.projectName
    def setProjectName(self, projectName):
        self.projectName = projectName

    def getProjectDescription(self):
        return self.projectDescription
    def setProjectDescription(self, projectDescription):
        self.projectDescription = projectDescription

    def getNumberOfProjects(self):
        return self.numberOfProjects

    def getPDT(self):
        return self.protocolDecisionTree
    def setPDT(self, protocolDecisionTree):
        self.protocolDecisionTree = protocolDecisionTree

    def getDissector(self):
        return self.dissector
    def setDissector(self, dissector):
        self.dissector = dissector

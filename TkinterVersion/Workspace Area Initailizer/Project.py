class Project:

    projectName = "Project1"
    projectDescription = "This is a project"
    numberOfProjects = 0
    #protocolDecisionTree = PDT
    #dissector = DissectorScript


    def __init__(self, projectName, projectDescription):
        self.projectName = projectName
        self.projectDescription = projectDescription
        Project.numberOfProjects += 1

    def getProjectName(self, projectName):
        return self.projectName
    def setProjectName(self, projectName):
        self.projectName = projectName

    def getProjectDescription(self, projectDescription):
        return self.projectDescription
    def setProjectDescription(self, projectDescription):
        self.projectDescription = projectDescription

    def getNumberOfProjects(self, numberOfProjects):
        return self.numberOfProjects

    def getPDT(self, protocolDecisionTree):
        return self.protocolDecisionTree
    def setPDT(self, protocolDecisionTree):
        self.protocolDecisionTree = protocolDecisionTree

    def getDissector(self, dissector):
        return self.dissector
    def setDissector(self, dissector):
        self.dissector = dissector

    #def exportAsXML(self):

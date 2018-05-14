import Project
import xml.etree.cElementTree as ET

class Workspace:

    workspaceName = "Workspace1"
    workspaceDirectory = "Desktop"
    projectList = []



    def __init__(self, workspaceName):
        self.workspaceName = workspaceName

    def saveProjectAsXML(self):

        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")

        ET.SubElement(doc, "field1Byte", name="Type", value = "anything").text = "1 Byte"
        ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

        tree = ET.ElementTree(root)
        tree.write("filename.xml")

    #def createProject(self, Project projectName):

    #def deleteProject(self, Project projectName):

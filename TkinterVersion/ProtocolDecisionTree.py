import Protocol
import FieldManager
import ConstructManager
import StartNode
import EndNode

class ProtocolDecisionTree():

    def __init__(self):

        self.Protocol = Protocol.Protocol()
        self.FieldManager = FieldManager.FieldManager()
        self.ConstructManager = ConstructManager.ConstructManager()
        self.StartNode = StartNode.StartNode("Name", "Protocol Desciption", "Dependent Protocol Name", "Dependency Pattern")
        self.EndNode = EndNode.EndNode()
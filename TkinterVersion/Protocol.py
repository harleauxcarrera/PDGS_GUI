class Protocol():

    def __init__(self):

        self.Name = "ICMP"
        self.Description = "Used for messages send through pings and replies"

    def setName(self, name):
        self.Name = name
    def getName(self):
        return self.Name
    def setDes(self, des):
        self.Description = des
    def getDes(self):
        return self.Description
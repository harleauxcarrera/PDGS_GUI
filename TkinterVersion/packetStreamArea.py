from Tkinter import *

class packetStreamArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Packet Stream Area")
        packetStreamFrame = Frame(self)
        packetStreamFrame.pack(fill=BOTH, expand=1)
        placeholder2 = Label(packetStreamFrame, text="PlaceHolder", bg="GRAY")
        placeholder2.pack(fill=BOTH, expand=1)
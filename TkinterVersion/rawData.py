from Tkinter import *

class rawData(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Raw Data Area")
        rawDataFrame = Frame(self)
        rawDataFrame.pack(fill=BOTH, expand=1)
        placeholder4 = Label(rawDataFrame, text="PlaceHolder", bg="GRAY")
        placeholder4.pack(fill=BOTH, expand=1)
from Tkinter import *

class dissectedStreamArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Dissected Stream Area")
        dissectedStreamFrame = Frame(self)
        dissectedStreamFrame.pack(fill=BOTH, expand=1)
        placeholder3 = Label(dissectedStreamFrame, text="PlaceHolder", bg="GRAY")
        placeholder3.pack(fill=BOTH, expand=1)
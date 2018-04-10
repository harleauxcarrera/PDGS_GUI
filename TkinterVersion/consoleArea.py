from Tkinter import *

class consoleArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Console Area")
        consoleFrame = Frame(self)
        consoleFrame.pack(fill=BOTH, expand=1)
        placeholder5 = Label(consoleFrame, text="PlaceHolder", bg="GRAY")
        placeholder5.pack(fill=BOTH, expand=1)
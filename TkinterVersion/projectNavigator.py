from Tkinter import *

class projectNavigator(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=200, height=700)
        self.title("Project Navigator")
        navigatorFrame = Frame(self)
        navigatorFrame.pack(fill=BOTH, expand=1)
        placeholder = Label(navigatorFrame, text="PlaceHolder", bg="GRAY")
        placeholder.pack(fill=BOTH, expand=1)
from Tkinter import *

class endFieldWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self)
        self.title("End Field Window")
        self.geometry("150x30")

        mainFrame = Frame(self)
        mainFrame.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)

        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)

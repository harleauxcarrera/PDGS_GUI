from Tkinter import *

class endFieldWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=300, height=30)
        self.title("End Field Window")

        mainFrame = Frame(self)
        mainFrame.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)

        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)

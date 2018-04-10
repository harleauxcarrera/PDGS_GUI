from Tkinter import *

class startFieldWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=300, height=150)
        self.title("Start Field Window")

        mainFrame = Frame(self)
        mainFrame.pack()

        protoName = Label(mainFrame, text="Protocol Name:")
        protoNameInput = Entry(mainFrame)

        protoDescr = Label(mainFrame, text="Protocol Description:")
        protoDescrInput = Entry(mainFrame)

        depProto = Label(mainFrame, text="Dependent Protocol Name:")
        depProtoInput = Entry(mainFrame)

        depPattern = Label(mainFrame, text="Dependency Pattern:")
        depPatternInput = Entry(mainFrame)

        protoName.grid(row=0, column=0)
        protoNameInput.grid(row=0, column=1)
        protoDescr.grid(row=1, column=0)
        protoDescrInput.grid(row=1, column=1)
        depProto.grid(row=2, column=0)
        depProtoInput.grid(row=2, column=1)
        depPattern.grid(row=3, column=0)
        depPatternInput.grid(row=3, column=1)

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)


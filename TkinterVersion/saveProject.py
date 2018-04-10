from Tkinter import *

class saveProject(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=200, height=150)
        self.title("Save Project")

        mainFrame = Frame(self)
        mainFrame.pack()

        titleLabel = Label(mainFrame, text="Create New Project")
        titleLabel.grid(row=0, column=0, columnspan=2)

        name = Label(mainFrame, text="Project Name")
        nameEntry = Entry(mainFrame)

        name.grid(row=1, column=0)
        nameEntry.grid(row=1, column=1)

        descr = Label(mainFrame, text="Description")
        descrEntry = Entry(mainFrame)

        descr.grid(row=2, column=0)
        descrEntry.grid(row=2, column=1)

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Create", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)
from Tkinter import *

class referenceListWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=300, height=250)
        self.title("Reference List Window")

        mainFrame = Frame(self)
        mainFrame.pack()

        name = Label(mainFrame, text="Reference List Name:")
        nameInput = Entry(mainFrame)
        name.grid(row=0, column=0)
        nameInput.grid(row=0, column=1)

        listBoxFrame = Frame(self)
        listBoxFrame.pack()

        listbox = Listbox(listBoxFrame, width=60)
        listbox.insert(1, "Random Reference Place Holder", "Second Place Holder")
        listbox.insert(2, "Another random one", "ZSGWEGWEGWEG")

        listbox.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)
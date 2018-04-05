from Tkinter import *

class referenceListWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self)
        self.title("Reference List Window")
        self.geometry("300x250")

        mainFrame = Frame(self)
        mainFrame.pack()

        name = Label(mainFrame, text="Reference List Name:")
        nameInput = Entry(mainFrame)
        name.grid(row=0, column=0)
        nameInput.grid(row=0, column=1)

        listBoxFrame = Frame(self)
        listBoxFrame.pack()

        listbox = Listbox(listBoxFrame)
        listbox.insert(1, "X", "Y")
        listbox.insert(2, "W", "Z")

        listbox.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)
from Tkinter import *

class packetInfoWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self)
        self.title("Packet Info Window")
        self.geometry("300x250")

        mainFrame = Frame(self)
        mainFrame.pack()

        listbox = Listbox(mainFrame)
        listbox.insert(1, "X", "Y")
        listbox.insert(2, "W", "Z")

        listbox.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)
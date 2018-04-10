from Tkinter import *

class packetInfoWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=300, height=250)
        self.title("Packet Info Window")

        mainFrame = Frame(self)
        mainFrame.pack()

        listbox = Listbox(mainFrame, width=60)
        listbox.insert(1, "Random Place Holder Packet", "Other Random Place Holder Packet")
        listbox.insert(2, "Another one", "One more")

        listbox.pack()

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)
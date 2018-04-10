from Tkinter import *
import ttk

class fieldWindow(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=300, height=250)
        self.title("Field Window")

        mainFrame = Frame(self)
        mainFrame.pack()

        name = Label(mainFrame, text="Name:")
        nameInput = Entry(mainFrame)

        abbrv = Label(mainFrame, text="Abbreviation:")
        abbrvInput = Entry(mainFrame)

        descr = Label(mainFrame, text="Description:")
        descrInput = Entry(mainFrame)

        ref = Label(mainFrame, text="Reference List:")
        refVal = StringVar()
        refInput = ttk.Combobox(mainFrame, textvariable=refVal)
        refInput['values'] = ("One", "Two", "Three")

        dataType = Label(mainFrame, text="Data Type:")
        dataTypeInput = ttk.Combobox(mainFrame)
        dataTypeInput['values'] = ("One", "Two", "Three")

        base = Label(mainFrame, text="Base:")
        baseInput = ttk.Combobox(mainFrame)
        baseInput['values'] = ("One", "Two", "Three")

        mask = Label(mainFrame, text="Mask:")
        maskInput = Entry(mainFrame)

        vconst = Label(mainFrame, text="Value Constraint:")
        vconstInput = Entry(mainFrame)

        req = Label(mainFrame, text="Required:")
        reqCheck = Checkbutton(mainFrame)

        buttonFrame = Frame(self)
        buttonFrame.pack(side=BOTTOM, fill=X, expand=1)
        okButton = Button(buttonFrame, text="Ok", command=self.withdraw)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.destroy)
        cancelButton.pack(side=RIGHT)
        okButton.pack(side=RIGHT)

        name.grid(row=0, column=0)
        nameInput.grid(row=0, column=1)
        abbrv.grid(row=1, column=0)
        abbrvInput.grid(row=1, column=1)
        descr.grid(row=2, column=0)
        descrInput.grid(row=2, column=1)
        ref.grid(row=3, column=0)
        refInput.grid(row=3, column=1)
        dataType.grid(row=4, column=0)
        dataTypeInput.grid(row=4, column=1)
        base.grid(row=5, column=0)
        baseInput.grid(row=5, column=1)
        mask.grid(row=6, column=0)
        maskInput.grid(row=6, column=1)
        vconst.grid(row=7, column=0)
        vconstInput.grid(row=7, column=1)
        req.grid(row=8, column=0)
        reqCheck.grid(row=8, column=1)



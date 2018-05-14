from Tkinter import *

class consoleArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Console Area")
        consoleFrame = Frame(self)
        consoleFrame.pack(fill=BOTH, expand=1)
        #placeholder5 = Label(consoleFrame, text="PlaceHolder", bg="GRAY")
        #placeholder5.pack(fill=BOTH, expand=1)


        #main_frame = Frame(consoleFrame)
        #main_frame.grid_columnconfigure(0, weight=1)
        #main_frame.grid(row=0, column=0, sticky="nsew")

        self.listbox_frame = Frame(consoleFrame)
        self.listbox_frame.grid(row=0, column=0, sticky="nsew")

        error_list = ['No error message to show.','Error number 1','Error number 2','Error number 3']
        scrollbar = Scrollbar(main, orient="vertical")
        self.listbox = Listbox(self.listbox_frame, selectmode='extended', bg='white', width=60, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=X, expand=True)

        for error in error_list:
            self.listbox.insert('end', error)
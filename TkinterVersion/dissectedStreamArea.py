from Tkinter import *
import Tkinter as tk

class dissectedStreamArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Dissected Stream Area")
        #window_prompt = tk.Message(self, text="Random Stuff")
        #window_prompt.pack(fill=BOTH)
        dissectedStreamFrame = Frame(self)
        dissectedStreamFrame.pack(fill=BOTH, expand=1)
        placeholder3 = Label(dissectedStreamFrame, text="PlaceHolder", bg="GRAY")
        placeholder3.pack(fill=BOTH, expand=1)
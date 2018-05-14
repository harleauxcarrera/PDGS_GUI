import Tkinter as tk

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Raw Data Area")
        self.master.resizable(True,True)
        self.master.tk_setPalette('#ececec')

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight())/3
        #center the frame on the screen
        self.master.geometry("+{}+{}".format(x,y))

        self.master.config(menu=tk.Menu(self))

        window_prompt = tk.Message(self, text="  00 10 33 17 36 e2 01 12  36 06 e3 7f 60 10 36 10   \n"
                                              " 01 13 43 23 45 a2 01 20  45 03 f3 e3 79 10 22 00   \n"
                                              "  00 1c 00 35 f5 98 00 85  98 5a cf 1f 81 80 00 01   \n"
                                              "  00 06 00 00 00 00 03 77  77 77 03 63 6e 6e 03 63   \n"
                                              "  6f 6d 00 00 01 00 01 c0  0c 00 01 00 01 00 00 00   \n"
                                              " b7 00 04 40 ec 5b 15 c0  0c 00 01 00 01 00 00 00   \n"
                                              "  b7 00 04 40 ec 5b 17 c0  0c 00 01 00 01 00 00 00   \n"
                                              "  b7 00 04 40 ec 10 14 c0  0c 00 01 00 01 00 00 00   "

                                   , font="System 14", justify='left',aspect=1200)
        window_prompt.pack(pady=(50, 50))


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()

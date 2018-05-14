from Tkinter import *

class rawData(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Raw Data Area")
        rawDataFrame = Frame(self)
        rawDataFrame.pack(fill=BOTH, expand=1)
        #placeholder4 = Label(rawDataFrame, text="PlaceHolder", bg="GRAY")
        #placeholder4.pack(fill=BOTH, expand=1)
        window_prompt = Message(rawDataFrame, text=" 00 10 33 17 36 e2 01 12  36 06 e3 \n"
                                              " 01 13 43 23 45 a2 01 20  45 03 f3 \n"
                                              " 00 1c 00 35 f5 98 00 85  98 5a cf \n"
                                              " 00 06 00 00 00 00 03 77  77 77 03 \n"
                                              " 6f 6d 00 00 01 00 01 c0  0c 00 01 \n"
                                              " b7 00 04 40 ec 5b 15 c0  0c 00 01 \n"
                                              " b7 00 04 40 ec 5b 17 c0  0c 00 01 \n"
                                              " b7 00 04 40 ec 10 14 c0  0c 00 01 \n"
                                              " 01 13 43 23 45 a2 01 20  45 03 f3 ", width=180, bg="white", anchor="nw")
        window_prompt.pack(fill=BOTH, expand=1)
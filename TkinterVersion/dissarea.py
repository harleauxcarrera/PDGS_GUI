from Tkinter import *

class rawData(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Dissected packet area")
        rawDataFrame = Frame(self)
        rawDataFrame.pack(fill=BOTH, expand=1)
        #placeholder4 = Label(rawDataFrame, text="PlaceHolder", bg="GRAY")
        #placeholder4.pack(fill=BOTH, expand=1)
        window_prompt = Message(rawDataFrame, text="[+]  Protocol: TCP Src:0030, Dst: 0080\n"
                                              "        [Request In: 673]\n"
                                              "        [Time: 0.0382669 s]\n"
                                               "        Authority RRs: 0\n"
                                               "        Additional RRs: 0\n"
                                              "        Transaction ID: 0xcf1f\n"
                                              "        Questions: 2\n"
                                              "        Answer RRs: 4\n"
                                              "    [-] Queries\n"
                                              "               Name: www.TShark.com\n"
                                              "               Type: Host Address\n"
                                              "               Class: IN (0x0fff)", width=180, bg="white", anchor="nw")
        window_prompt.pack(fill=BOTH, expand=1)

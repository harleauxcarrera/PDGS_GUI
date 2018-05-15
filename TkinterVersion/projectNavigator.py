from Tkinter import *
import ttk

class projectNavigator(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=200, height=700)
        self.title("Project Navigator")
        self.navigatorFrame = Frame(self)
        self.navigatorFrame.pack(fill=BOTH, expand=1)
        #placeholder = Label(navigatorFrame, text="PlaceHolder", bg="GRAY")
        #placeholder.pack(fill=BOTH, expand=1)

        self.treeframe = Frame(self.navigatorFrame)
        self.treeframe.pack(anchor="w", expand=1, fill=X)

        self.tree = ttk.Treeview(self.treeframe, selectmode=NONE, height=600)
        self.tree.pack(fill=BOTH, expand=1)
        self.tree.bind("<Double-1>", self.OnDoubleClick)

        self.tree.heading("#0", text="First Workspace", anchor="center")

        self.img1 = PhotoImage(file="open_folder_icon.gif")
        self.img1 = self.img1.subsample(10,10)

        project1 = self.tree.insert("", "end", text="ICMP Project", image=self.img1)
        self.tree.insert(project1, "end", text="ICMP Dissector")
        self.tree.insert(project1, "end", text="ICMP PCAP")

        project2 = self.tree.insert('', 'end', text="Project Two", image=self.img1)
        self.tree.insert(project2, 'end', text="Second Dissector")

        project3 = self.tree.insert('', 'end', text="Project Three", image=self.img1)
        self.tree.insert(project3, 'end', text="Third Dissector")

        project4 = self.tree.insert('', 'end', text="Project Four", image=self.img1)
        self.tree.insert(project4, 'end', text="Fourth Dissector")

        project5 = self.tree.insert('', 'end', text="Project Five", image=self.img1)
        self.tree.insert(project5, 'end', text="Fifth Dissector")

    def OnDoubleClick(self, event):
        item = self.tree.identify('item', event.x, event.y)
        print("you clicked on", self.tree.item(item, "text"))